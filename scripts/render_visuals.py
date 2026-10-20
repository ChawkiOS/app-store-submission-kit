#!/usr/bin/env python3
"""Renders every store visual, in each language, from a visuals.json file.

Usage: python3 render_visuals.py visuals.json [--lang en] [--only screenshots|banners|icon]

Paths in visuals.json are relative to the folder containing that file (usually the project root).
Commented template: ../template/visuals.json. Rendered with headless Chrome (Google Fonts: Internet required).

Files produced (in "output", store/ by default):
  <lang>/ios/screenshots-6.9/<n>.png        1320 × 2868  (Apple, iPhone 6.9" tab)
  <lang>/ios/screenshots-6.3/<n>.png        1206 × 2622  (Apple, only if Apple asks for it)
  <lang>/ios/header-5244x2950.png           Apple header
  <lang>/ios/header-3840x1646.png           Apple header, panoramic format
  <lang>/ios/search-5244x2950.png           Apple search results artwork (variant on accent background)
  <lang>/android/screenshots/<n>.png        1080 × 1920  (Google Play, phone)
  <lang>/android/feature-graphic-1024x500.png  Google Play feature graphic
  android/icon-512.png                      Google Play icon, no transparency
  <lang>/contact-sheet.png                  contact sheet: everything shrunk onto one image, to look at before delivering
"""
import json
import os
import shutil
import struct
import subprocess
import sys
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE.parent / 'visual-templates'

SCREENSHOTS = [('ios/screenshots-6.9', 1320, 2868, None), ('ios/screenshots-6.3', 1206, 2622, None), ('android/screenshots', 1080, 1920, 'google')]
BANNERS = [
    ('ios/header-5244x2950.png', 5244, 2950, {}),
    ('ios/header-3840x1646.png', 3840, 1646, {'wide': '1'}),
    ('ios/search-5244x2950.png', 5244, 2950, {'variant': 'accent'}),
    ('android/feature-graphic-1024x500.png', 1024, 500, {}),
]


def chrome() -> str:
    for c in ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', shutil.which('google-chrome') or '', shutil.which('chromium') or '', shutil.which('chromium-browser') or '']:
        if c and os.path.exists(c):
            return c
    sys.exit('Google Chrome not found.')


def png_size(path: Path):
    with open(path, 'rb') as f:
        header = f.read(24)
    return struct.unpack('>II', header[16:24])


def render(page: Path, params: dict, width: int, height: int, output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    url = page.as_uri() + '?' + urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, '')})
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    f'--window-size={width},{height}', '--virtual-time-budget=8000', '--allow-file-access-from-files',
                    f'--screenshot={output}', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    if not output.exists():
        sys.exit(f'Render failed: {output}')
    w, h = png_size(output)
    if (w, h) != (width, height):
        sys.exit(f'{output} is {w} × {h} instead of {width} × {height}')
    print(f'  {output}  {w} × {h}')


def file_uri(base: Path, path: str) -> str:
    p = (base / path).resolve()
    if not p.exists():
        sys.exit(f'Image not found: {p}')
    return p.as_uri()


def contact_sheet(images: list, output: Path):
    # Every image of a language shrunk side by side, to look at them all at once.
    html = output.with_suffix('.html')
    cells = ''.join(f'<figure><img src="{Path(i).resolve().as_uri()}"><figcaption>{Path(i).parent.name}/{Path(i).name}</figcaption></figure>' for i in images)
    html.write_text('<body style="margin:0;padding:16px;background:#777;font:14px sans-serif;color:#fff;display:flex;flex-wrap:wrap;gap:16px;align-items:flex-end">'
                    '<style>figure{margin:0}img{display:block;max-height:640px;max-width:1100px}</style>' + cells + '</body>')
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=2400,2200', '--virtual-time-budget=4000',
                    '--allow-file-access-from-files', f'--screenshot={output}', html.as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    html.unlink()
    print(f'  {output}  (contact sheet)')


def main():
    arguments = sys.argv[1:]
    if not arguments:
        sys.exit(__doc__)
    config_path = Path(arguments[0]).resolve()
    base = config_path.parent
    only_lang = arguments[arguments.index('--lang') + 1] if '--lang' in arguments else None
    only = arguments[arguments.index('--only') + 1] if '--only' in arguments else None
    c = json.loads(config_path.read_text(encoding='utf-8'))

    output = base / c.get('output', 'store')
    colors = c.get('colors', {})
    fonts = c.get('fonts', {})
    common = {
        'background': colors.get('background'), 'text': colors.get('text'), 'accent': colors.get('accent'), 'partner': colors.get('partner'),
        'title-font': fonts.get('title'), 'text-font': fonts.get('text'),
    }

    if only in (None, 'icon') and c.get('icon'):
        print('Google Play icon')
        page = output / '_icon.html'
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(f'<body style="margin:0;background:{colors.get("background", "#fff")}"><img src="{file_uri(base, c["icon"])}" style="width:100vw;height:100vh;display:block;object-fit:cover"></body>')
        render(page, {}, 512, 512, output / 'android' / 'icon-512.png')
        page.unlink()

    for lang, l in c['languages'].items():
        if only_lang and lang != only_lang:
            continue
        print(f'\n== {lang}')
        produced = []
        if only in (None, 'screenshots'):
            for n, shot in enumerate(l.get('screenshots', []), 1):
                params = dict(common)
                params.update({
                    'screen': file_uri(base, shot['screen']), 'label': shot.get('label'), 'title': shot.get('title'), 'subtitle': shot.get('subtitle'),
                    'angle': shot.get('angle', '-2deg' if n % 2 else '2deg'), 'ratio': c.get('screen_ratio', '1320 / 2868'),
                    'stickers': json.dumps(shot.get('stickers', []), ensure_ascii=False),
                })
                if shot.get('background'):
                    params['background'] = shot['background']
                if shot.get('title_accent'):
                    params['title-accent'] = shot['title_accent']
                for folder, width, height, phone_format in SCREENSHOTS:
                    p = dict(params)
                    if phone_format:
                        p['format'] = phone_format
                    target = output / lang / folder / f'{n}.png'
                    render(TEMPLATES / 'screenshot.html', p, width, height, target)
                    if folder != 'ios/screenshots-6.3':
                        produced.append(target)
        if only in (None, 'banners') and l.get('banner'):
            b = l['banner']
            params = dict(common)
            params.update({
                'name': c.get('name'), 'tagline': b.get('tagline'), 'pill': b.get('pill'),
                'artwork': file_uri(base, c.get('artwork') or c['icon']), 'artwork-fill': '1' if c.get('artwork_fill') or not c.get('artwork') else '0',
                'bubbles': json.dumps(b.get('bubbles', []), ensure_ascii=False),
            })
            for file_name, width, height, extra in BANNERS:
                target = output / lang / file_name
                render(TEMPLATES / 'banner.html', {**params, **extra}, width, height, target)
                produced.append(target)
        if produced:
            contact_sheet(produced, output / lang / 'contact-sheet.png')
    print('\nLook at each contact sheet (and at the full-size images if in doubt) before delivering.')


if __name__ == '__main__':
    main()
