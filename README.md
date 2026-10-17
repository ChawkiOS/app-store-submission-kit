# fiches-stores

An agent skill for [Claude Code](https://claude.com/claude-code) that prepares **everything you need to submit an app to the App Store and Google Play**, starting from your app's specification and mockups:

- **Store listing texts in the languages you choose**: name, subtitle, short and full descriptions, promotional text, keywords, release notes, each one written for its language, not translated word for word.
- **Answers to every console questionnaire**: categories and tags, Apple age rating, Google IARC content rating (question by question), Apple App Privacy, Google Data safety, target audience, content rights, encryption, ads, advertising ID, financial and health features, and more. Each answer comes with the reason behind it.
- **Review and testing**: App Review notes, reviewer contact details, TestFlight setup, Google internal and closed testing (including the 12-testers-for-14-days rule), and instructions for your testers.
- **All store visuals, rendered at the exact required sizes, in every language**: iPhone screenshots, Android screenshots, Apple header and search artwork, Google feature graphic and 512 px icon, plus one contact sheet per language so you can check everything at a glance.

Everything ends up in one verified `STORE.md` file and a ready-to-upload `store/` folder. You should never have to stare at a console form wondering what to answer, or open a design tool to make a screenshot.

> The skill's instructions and references are written in French (it was built while shipping a French app), but it writes store listings in any language you ask for, and Claude follows the instructions just as well when you talk to it in English.

## What you get

```
your-project/
├── STORE.md                    # every field for both consoles, every language, with reasons
├── visuels.json                # brand + captions per language (re-render anytime)
└── store/
    ├── captures-brutes/<lang>/ # raw app screens used for the screenshots
    ├── android/icone-512.png   # Google Play icon
    └── <lang>/
        ├── planche.png         # contact sheet: all visuals for this language
        ├── ios/
        │   ├── captures-6.9/   # 1320 × 2868 (iPhone 6.9")
        │   ├── captures-6.3/   # 1206 × 2622 (iPhone 6.3", only if Apple asks)
        │   ├── entete-5244x2950.png
        │   ├── entete-3840x1646.png
        │   └── recherche-5244x2950.png
        └── android/
            ├── captures/       # 1080 × 1920
            └── banniere-1024x500.png
```

## Requirements

- **[Claude Code](https://claude.com/claude-code)**, or any agent that loads `SKILL.md` skills.
- **Python 3.9+** for the two helper scripts (standard library only, nothing to install).
- **Google Chrome** for rendering the visuals: macOS app, or `google-chrome` / `chromium` on Linux.
- **An internet connection** while rendering, because fonts are loaded from Google Fonts.

## Installation

Clone the repository into your skills folder.

**For all your projects (user level):**

```bash
git clone https://github.com/<you>/fiches-stores.git ~/.claude/skills/fiches-stores
```

**For a single project (shared with your team through the repo):**

```bash
git clone https://github.com/<you>/fiches-stores.git .claude/skills/fiches-stores
```

Then start a new Claude Code session. The skill shows up in the skills list as `fiches-stores`. To update it later, run `git pull` in that folder.

## Usage

In your app's project, ask Claude Code in plain words, or call the skill directly:

```
/fiches-stores
```

```
Prepare the App Store and Google Play listings in English, Spanish and French.
The mockups are in docs/mockups/.
```

```
Prépare les fiches des stores en anglais et en français, avec les visuels.
```

The skill then works in this order:

1. **Asks for the languages and the mockups** (unless your request already gives them), plus at most a few missing facts: contact e-mail, publisher name, brand colors… Each question comes with a suggested default.
2. **Reads your project**: specification, app config (`app.json`, `Info.plist`, `AndroidManifest.xml`), translation files, privacy policy, theme, and the code wherever it answers a questionnaire (ad or analytics SDKs, accounts, data sent to servers, user-generated content).
3. **Writes `STORE.md`** from the template, one section per language.
4. **Produces the visuals.** It gathers one app screen per screenshot and per language, writes `visuels.json`, renders everything, looks at each contact sheet and fixes anything that overflows or reads badly.
5. **Checks everything**: character limits and Apple keyword rules, and consistency between the listing, the code and the privacy policy.
6. **Stays with you in the consoles**: paste any question from App Store Connect or the Play Console and it answers with the exact value to pick and a one-line reason.

### Mockups it accepts

- **Real screenshots of your app**: the best option, since Apple wants screenshots that show the actual app.
- **Mockup images**: PNG, JPG or PDF.
- **An HTML page or Claude artifact** with your mockups. Each screen is rendered at phone size.
- **A Figma link**, through the Figma skill if you have it.
- **None.** The skill tells you how to capture the app on a phone in demo mode, in each language.

## Using the scripts on their own

**Check a `STORE.md`** (character limits, Apple keywords):

```bash
python3 ~/.claude/skills/fiches-stores/scripts/verifier_store.py STORE.md
```

Fields are recognized by their bold label with a limit, followed by a quote:

```markdown
**App Store subtitle** (30 characters max):

> The hot potato game with friends
```

**Render all visuals** from a `visuels.json` (start from [`modele/visuels.json`](modele/visuels.json)):

```bash
python3 ~/.claude/skills/fiches-stores/scripts/rendre_visuels.py visuels.json
python3 ~/.claude/skills/fiches-stores/scripts/rendre_visuels.py visuels.json --langue en
python3 ~/.claude/skills/fiches-stores/scripts/rendre_visuels.py visuels.json --seulement captures   # or bannieres, icone
```

`visuels.json` in short:

| Key | Meaning |
| --- | --- |
| `nom` | App name shown on the banners |
| `icone` | App icon (used for the 512 px Google icon, and on banners when there is no `visuel`) |
| `visuel` | Mascot or logo shown in the banner circle; `visuel_plein: true` to fill the circle |
| `couleurs` | `fond` (background), `texte`, `accent`, `partenaire` (second brand color) |
| `polices` | `titre` and `texte`: any Google Fonts family |
| `ratio_ecran` | Aspect ratio of your raw screens, default `1320 / 2868` |
| `langues.<code>.banniere` | `accroche` (tagline), `pastille` (pill), `bulles` (up to 2 speech bubbles) |
| `langues.<code>.captures[]` | `ecran` (raw screen), `etiquette` (label), `titre` (`<em>word</em>` is highlighted), `sous` (subtitle), `fond`, `accent_titre`, `autocollants` (stickers: text, position, angle, color) |

Paths are relative to `visuels.json`. If your brand needs a very different look, copy `modeles-visuels/` into your project and edit the HTML; the script passes the same parameters.

## What's inside

| Path | Purpose |
| --- | --- |
| `SKILL.md` | The workflow Claude follows |
| `references/apple.md` | App Store Connect field by field: limits, categories, age rating, App Privacy, review guidelines that cause rejections, review notes template, TestFlight |
| `references/google.md` | Play Console field by field: listing, categories and tags, App content, IARC walkthrough, Data safety, target audience, testing tracks, service account setup for `eas submit` |
| `references/langues.md` | Locale codes for both stores, regional variants, how to adapt texts and keywords |
| `references/visuels.md` | Exact visual sizes and screenshot rules |
| `modele/STORE.md` | Template of the output file |
| `modele/visuels.json` | Commented example of the visuals config |
| `modeles-visuels/` | HTML templates for screenshots and banners |
| `scripts/verifier_store.py` | Checks `STORE.md` |
| `scripts/rendre_visuels.py` | Renders every visual in every language |

## Good to know

- **Store rules change often.** The references are dated (October 2026). When a console shows something different, the console wins, and the skill tells you so.
- **You stay responsible for what you submit.** Read the answers about age rating and privacy before you paste them: they must match what your app really does.
- **Expo-friendly.** It knows `app.json`, EAS Build and `eas submit`, but works for any iOS or Android project.
- This project is not affiliated with Apple or Google. App Store, App Store Connect, TestFlight, Google Play and Play Console are trademarks of their respective owners.

## Contributing

Issues and pull requests are welcome, especially when a console changes a field, a limit or a questionnaire. Please mention the date and which console you saw it in.
