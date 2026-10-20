---
name: fiches-stores
description: Prepares EVERYTHING needed to publish a mobile app, built with any technology (native, React Native, Flutter…), on the App Store and Google Play from a spec and mockups — listing texts in the chosen languages (name, subtitle, descriptions, keywords, promotional text, release notes), categories and tags, URLs, answers to every questionnaire (Apple age rating and IARC, Apple privacy, Google data safety, app content, rights, encryption), review notes, internal and closed testing, and visuals rendered at exact sizes in each language (iPhone and Android screenshots, Apple header and search artwork, Google feature graphic and icon), in a verified STORE.md and store/ folder. Use when the user asks to prepare, write or fill an App Store / Google Play listing, store screenshots, feature graphic, description, keywords, metadata, age rating, privacy or data safety answers, review notes, TestFlight or closed testing, or "la fiche store", "les fiches des stores", "les visuels des stores", "préparer la soumission".
---

# App Store and Google Play listings and visuals

From the app's specification and mockups, produces:

1. **`STORE.md`** at the project root: every field of both consoles, in each chosen language, with its ready-to-paste answer and its reason.
2. **`store/`**: every visual at the exact size, in each language, ready to upload, with one contact sheet per language.

The user should never have to think in front of a form or open a design tool.

Works with any mobile technology: native iOS and Android, React Native (CLI or Expo), Flutter, Kotlin Multiplatform, Ionic / Capacitor, Cordova, NativeScript, .NET MAUI, Unity, Godot…

References (read the one for the current step):

- [references/frameworks.md](references/frameworks.md): per technology, where to find the facts, common settings, how to build and upload.
- [references/languages.md](references/languages.md): language codes for both stores, adaptation, regional variants.
- [references/apple.md](references/apple.md): App Store Connect, field by field.
- [references/google.md](references/google.md): Play Console, field by field, IARC questionnaire step by step.
- [references/visuals.md](references/visuals.md): exact sizes and rules for visuals.
- [template/STORE.md](template/STORE.md) and [template/visuals.json](template/visuals.json): skeletons to fill in.
- `scripts/check_store.py`: character limits and keywords.
- `scripts/render_visuals.py` (with `visual-templates/`): renders every visual, in every language.

Store rules change. References are current as of October 2026; if the console shows something else, the console is right: adapt and say so.

## 1. Ask for the languages and the mockups (always, first)

Before writing anything, make sure you have these two answers. If the user already gave them in the request ("prepare the listing in English, Spanish and French"), do not ask again.

1. **Which languages should the listings be prepared in?** Suggest the languages the app already contains (translation files), and remind the user that a listing in a language the app does not have misleads users (see references/languages.md). Specify the variant when it matters (Latin American or European Spanish, Brazilian or European Portuguese) and the **primary language** of the listing.
2. **Where are the mockups or screens?** Accept anything that shows the app:
   - **real screenshots** of the app (best: Apple wants screenshots that show the app as it is);
   - **mockup images** (PNG, JPG, PDF);
   - an **artifact or HTML page** of mockups (read it with the Artifact tool or open it, then render each screen at 1320 × 2868 with Chrome);
   - a **Figma** link (use the figma skill to export the screens);
   - otherwise, offer to capture the app on a phone, the iOS Simulator or an Android emulator (in demo mode, in each language; see references/visuals.md).
   If the project does not provide them, also ask for: brand colors and fonts, mascot or logo for the banners.

Ask these questions **in a single message**, together with the other missing facts from step 2 (5 questions at most in total, each with a suggested default).

## 2. Gather the facts

First **detect the technology** the app is built with (references/frameworks.md, "Detecting the technology"); its row in that file says where each fact below lives.

Then read, in the project: the specification (SPECIFICATION.md, README, docs), the app config and native config (`Info.plist`, `AndroidManifest.xml`, Gradle files, and the framework's own config), the dependencies, the privacy manifests, the translation files, the website (privacy, terms), the theme (colors, fonts), and the code wherever it answers a question.

| Fact | Where to find it |
| --- | --- |
| Technology (native, React Native, Flutter, …) | project files (references/frameworks.md) |
| Name, iOS bundle ID, Android package, version | app config |
| Platforms and devices: iPhone only or iPad too, Android phone or tablet | Xcode device family, framework config |
| What the app does, for whom, what makes it different | specification |
| Languages available in the app | translation files |
| Free or paid, in-app purchases, subscriptions, ads | specification, dependencies (ad SDKs, RevenueCat, StoreKit, Play Billing) |
| Account: none, anonymous, e-mail, Sign in with Apple/Google | authentication code |
| Data collected, why, providers (Firebase, Supabase, Sentry, analytics, backend…) | code, dependencies, privacy manifests, privacy policy |
| Content between users (free text, photos, chat), blocking, reporting | code, specification |
| Minimum age, target audience | terms, specification |
| Native permissions actually requested | final built manifest and Info.plist (libraries add some) |
| Third-party content (sounds, fonts, images) and licenses | assets, specification |
| URLs: website, support (with a contact), privacy, account deletion | website |
| Contact, publisher, copyright | website, user |
| How a reviewer can test the app alone (demo, solo mode, video) | specification |
| Colors, fonts, logo, mascot | theme, assets |

**Never invent anything**: a fact you cannot find becomes a question (step 1).

## 3. Write STORE.md

Start from [template/STORE.md](template/STORE.md). Sections, in the order the consoles are filled in:

1. **Writing rules** specific to the app.
2. **Texts, one section per language** (primary language first): App Store name, Google Play name, subtitle, short description, promotional text, full description, keywords, release notes. Each language is **written for itself** (references/languages.md), with its own keywords.
3. **Categories and tags**.
4. **URLs and contact**.
5. **Age**: Apple questionnaire, IARC step by step, target audience.
6. **Privacy**: Apple, then Google data safety.
7. **Declarations**: content rights, encryption, ads, app access, financial features, health, news, government, advertising ID.
8. **Review**: notes in English, contact details, Google access.
9. **Build and testing**: how to build and upload with the app's technology (references/frameworks.md), TestFlight, Google internal and closed testing (12 testers for 14 days for a recent personal account), instructions to testers in their languages.
10. **Visuals**: list of files produced per language (step 4).
11. Submission **checklist**.

Text rules:
- First sentence of the description = the hook (the only part visible before "more"). Then short sections with uppercase headings, bullets, a call to action.
- Concrete (what you do in the app) rather than adjectives; true (only the submitted version; "coming soon" only in Apple's promotional text).
- Apple keywords: 100 characters, commas without spaces, without repeating the name, subtitle or category, no third-party brands.
- No emoji in Apple texts. Gender-neutral when the language allows it.

Answer rules:
- Every answer gives its **reason**. Honest rather than flattering (an understated answer gets the app rejected or removed later).
- Consistent with the privacy policy, the code and the other store; flag any contradiction.
- Labels as they appear in the console (in the console's language; when in doubt, give both English and the user's language).

## 4. Produce the visuals

1. **Screens**: gather one screen per screenshot and per language in `store/raw-screens/<lang>/` (1320 × 2868 preferably; another phone size works, the frame adapts with `screen_ratio`). From the running app: capture on a device, simulator or emulator (references/visuals.md). From an HTML mockup: render each screen with headless Chrome at phone size. Only retouch what does not misrepresent the app (test usernames, demo data).
2. **Pick 4 to 6 screenshots** in the order of the journey that makes people want the app (references/visuals.md), each with: label, title (one word highlighted with `<em>`), sentence, background color, one sticker. Write them **in each language**.
3. **Fill in `visuals.json`** at the project root from [template/visuals.json](template/visuals.json): name, icon, mascot or logo, brand colors and fonts, and for each language the banner (tagline, pill, 2 bubbles) and the screenshots.
4. **Render**:

   ```bash
   python3 ~/.claude/skills/fiches-stores/scripts/render_visuals.py visuals.json
   ```

   Produces for each language: Apple 6.9" and 6.3" screenshots, Google screenshots, Apple header 5244 × 2950 and 3840 × 1646, Apple search artwork 5244 × 2950, Google feature graphic 1024 × 500; plus the Google 512 icon and one `contact-sheet.png` per language. `--lang en` or `--only screenshots|banners|icon` to redo part of it.
5. **Look at each contact sheet** (Read the image, shrunk with `sips -Z` if it is large): text that overflows or gets cut, a lone word at the end of a title, a sticker hiding important information, contrast. Fix `visuals.json` and redo the affected part until everything is clean.
6. If the brand does not fit the templates (very different style), copy `visual-templates/` into the project and adapt the HTML; the script passes the same parameters.

## 5. Check

```bash
python3 ~/.claude/skills/fiches-stores/scripts/check_store.py STORE.md
```

Fix until "Everything is within limits." Then reread as a reviewer would: does every promise exist in the app? Does every privacy answer match the code and the policy?

## 6. Deliver

- `STORE.md` (update the existing one, keeping what is already validated) and `store/` (with `visuals.json` and the raw screens, so everything can be redone).
- In the message: the languages covered, the files produced, the **choices to validate** (category, age, display name, screenshots), the sensitive answers to reread (age, privacy) and what is missing.
- Then walk the user through the consoles screen by screen: when they paste a form question, answer with the exact value to choose and the reason in one line, in the language of the question.
