#!/usr/bin/env python3
"""Rend tous les visuels des stores, dans chaque langue, à partir d'un fichier visuels.json.

Usage : python3 rendre_visuels.py visuels.json [--langue fr] [--seulement captures|bannieres|icone]

Les chemins de visuels.json sont relatifs au dossier qui contient ce fichier (en général la racine du projet).
Modèle commenté : ../modele/visuels.json. Rendu avec Chrome sans interface (Google Fonts : il faut Internet).

Fichiers produits (dans "sortie", par défaut store/) :
  <langue>/ios/captures-6.9/<n>.png        1320 × 2868  (Apple, onglet iPhone 6,9 pouces)
  <langue>/ios/captures-6.3/<n>.png        1206 × 2622  (Apple, seulement si Apple le demande)
  <langue>/ios/entete-5244x2950.png        en-tête Apple
  <langue>/ios/entete-3840x1646.png        en-tête Apple, format panoramique
  <langue>/ios/recherche-5244x2950.png     visuel des résultats de recherche Apple (variante sur fond d'accent)
  <langue>/android/captures/<n>.png        1080 × 1920  (Google Play, téléphone)
  <langue>/android/banniere-1024x500.png   bannière Google Play (feature graphic)
  android/icone-512.png                    icône Google Play, sans transparence
  <langue>/planche.png                     planche de contrôle : tout réduit sur une image, à regarder avant de livrer
"""
import json
import os
import shutil
import struct
import subprocess
import sys
import urllib.parse
from pathlib import Path

ICI = Path(__file__).resolve().parent
MODELES = ICI.parent / 'modeles-visuels'

CAPTURES = [('ios/captures-6.9', 1320, 2868, None), ('ios/captures-6.3', 1206, 2622, None), ('android/captures', 1080, 1920, 'google')]
BANNIERES = [
    ('ios/entete-5244x2950.png', 5244, 2950, {}),
    ('ios/entete-3840x1646.png', 3840, 1646, {'large': '1'}),
    ('ios/recherche-5244x2950.png', 5244, 2950, {'variante': 'accent'}),
    ('android/banniere-1024x500.png', 1024, 500, {}),
]


def chrome() -> str:
    for c in ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', shutil.which('google-chrome') or '', shutil.which('chromium') or '', shutil.which('chromium-browser') or '']:
        if c and os.path.exists(c):
            return c
    sys.exit('Google Chrome introuvable.')


def taille_png(chemin: Path):
    with open(chemin, 'rb') as f:
        entete = f.read(24)
    return struct.unpack('>II', entete[16:24])


def rendre(page: Path, params: dict, largeur: int, hauteur: int, sortie: Path):
    sortie.parent.mkdir(parents=True, exist_ok=True)
    url = page.as_uri() + '?' + urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, '')})
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                    f'--window-size={largeur},{hauteur}', '--virtual-time-budget=8000', '--allow-file-access-from-files',
                    f'--screenshot={sortie}', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    if not sortie.exists():
        sys.exit(f'Rendu raté : {sortie}')
    l, h = taille_png(sortie)
    if (l, h) != (largeur, hauteur):
        sys.exit(f'{sortie} fait {l} × {h} au lieu de {largeur} × {hauteur}')
    print(f'  {sortie}  {l} × {h}')


def fichier(base: Path, chemin: str) -> str:
    p = (base / chemin).resolve()
    if not p.exists():
        sys.exit(f'Image introuvable : {p}')
    return p.as_uri()


def planche(images: list, sortie: Path):
    # Toutes les images d'une langue réduites côte à côte, pour les regarder d'un coup.
    html = sortie.with_suffix('.html')
    cases = ''.join(f'<figure><img src="{Path(i).resolve().as_uri()}"><figcaption>{Path(i).parent.name}/{Path(i).name}</figcaption></figure>' for i in images)
    html.write_text('<body style="margin:0;padding:16px;background:#777;font:14px sans-serif;color:#fff;display:flex;flex-wrap:wrap;gap:16px;align-items:flex-end">'
                    '<style>figure{margin:0}img{display:block;max-height:640px;max-width:1100px}</style>' + cases + '</body>')
    subprocess.run([chrome(), '--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=2400,2200', '--virtual-time-budget=4000',
                    '--allow-file-access-from-files', f'--screenshot={sortie}', html.as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    html.unlink()
    print(f'  {sortie}  (planche de contrôle)')


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    config_chemin = Path(args[0]).resolve()
    base = config_chemin.parent
    seule_langue = args[args.index('--langue') + 1] if '--langue' in args else None
    seulement = args[args.index('--seulement') + 1] if '--seulement' in args else None
    c = json.loads(config_chemin.read_text(encoding='utf-8'))

    sortie = base / c.get('sortie', 'store')
    couleurs = c.get('couleurs', {})
    polices = c.get('polices', {})
    commun = {
        'fond': couleurs.get('fond'), 'texte': couleurs.get('texte'), 'accent': couleurs.get('accent'), 'partenaire': couleurs.get('partenaire'),
        'police-titre': polices.get('titre'), 'police-texte': polices.get('texte'),
    }

    if seulement in (None, 'icone') and c.get('icone'):
        print('Icône Google Play')
        page = sortie / '_icone.html'
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(f'<body style="margin:0;background:{couleurs.get("fond", "#fff")}"><img src="{fichier(base, c["icone"])}" style="width:100vw;height:100vh;display:block;object-fit:cover"></body>')
        rendre(page, {}, 512, 512, sortie / 'android' / 'icone-512.png')
        page.unlink()

    for langue, l in c['langues'].items():
        if seule_langue and langue != seule_langue:
            continue
        print(f'\n== {langue}')
        produits = []
        if seulement in (None, 'captures'):
            for n, cap in enumerate(l.get('captures', []), 1):
                params = dict(commun)
                params.update({
                    'ecran': fichier(base, cap['ecran']), 'etiquette': cap.get('etiquette'), 'titre': cap.get('titre'), 'sous': cap.get('sous'),
                    'angle': cap.get('angle', '-2deg' if n % 2 else '2deg'), 'ratio': c.get('ratio_ecran', '1320 / 2868'),
                    'autocollants': json.dumps(cap.get('autocollants', []), ensure_ascii=False),
                })
                if cap.get('fond'):
                    params['fond'] = cap['fond']
                if cap.get('accent_titre'):
                    params['accent-titre'] = cap['accent_titre']
                for dossier, largeur, hauteur, fmt in CAPTURES:
                    p = dict(params)
                    if fmt:
                        p['format'] = fmt
                    cible = sortie / langue / dossier / f'{n}.png'
                    rendre(MODELES / 'capture.html', p, largeur, hauteur, cible)
                    if dossier != 'ios/captures-6.3':
                        produits.append(cible)
        if seulement in (None, 'bannieres') and l.get('banniere'):
            b = l['banniere']
            params = dict(commun)
            params.update({
                'nom': c.get('nom'), 'accroche': b.get('accroche'), 'pastille': b.get('pastille'),
                'visuel': fichier(base, c.get('visuel') or c['icone']), 'visuel-plein': '1' if c.get('visuel_plein') or not c.get('visuel') else '0',
                'bulles': json.dumps(b.get('bulles', []), ensure_ascii=False),
            })
            for nom_fichier, largeur, hauteur, extra in BANNIERES:
                cible = sortie / langue / nom_fichier
                rendre(MODELES / 'banniere.html', {**params, **extra}, largeur, hauteur, cible)
                produits.append(cible)
        if produits:
            planche(produits, sortie / langue / 'planche.png')
    print('\nRegarder chaque planche (et les images en taille réelle au moindre doute) avant de livrer.')


if __name__ == '__main__':
    main()
