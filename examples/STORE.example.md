# Bloomly — App Store and Google Play listings

Example output of the skill for a fictional app. Last updated: 2026-10-20 (version 1.0.0).

Technology: Flutter. Bundle ID: com.bloomly.app. Package: com.bloomly.app. Devices: iPhone, Android phone (no iPad, no tablet layout).

Rules:

- The name is always written **Bloomly**.
- No emoji in App Store texts (rejected by Apple).
- Only mention what is in the submitted version (no shared households yet: "coming soon" only in the promotional text).
- Warm, practical tone; "you", never "users". No promise that plants cannot die.

## English (primary)

**App Store name** (30 characters max):

> Bloomly: Plant Care

**Google Play name** (30 characters max):

> Bloomly - Plant Watering

**App Store subtitle** (30 characters max):

> Water reminders for every pot

**Google Play short description** (80 characters max):

> Never forget to water again: smart reminders and care tips for every plant.

**App Store promotional text** (170 characters max, editable without an update):

> New: snap a leaf and Bloomly suggests the right watering rhythm. Coming soon: shared plants for the whole household.

**Full description** (4,000 characters max):

> **Bloomly tells you when each of your plants needs water, so none of them gets forgotten or drowned.**
>
> Add a plant in ten seconds with a photo, pick its type and pot size, and Bloomly builds its watering rhythm. A gentle reminder arrives on the right day, for the right plant.
>
> **A RHYTHM FOR EVERY PLANT**
>
> • 300+ plant types with their own watering, light and feeding needs
> • Pot size and season taken into account
> • Snooze a reminder when the soil is still wet: the rhythm adapts
>
> **YOUR JUNGLE AT A GLANCE**
>
> • Today's to-do list: water, mist, feed, repot
> • A photo diary for each plant to watch it grow
> • Rooms to group plants by window or floor
>
> **SIMPLE AND PRIVATE**
>
> • Works without an account; sign in with Apple or Google only to sync between devices
> • No ads, ever
> • Bloomly Plus (one-time purchase) unlocks unlimited plants and the leaf scanner
>
> Add your first plant and let Bloomly remember for you.

**App Store keywords** (100 characters max, comma-separated, no spaces):

> houseplant,greenery,garden,succulent,orchid,fern,cactus,schedule,gardening,indoor,leaf,botany

**Release notes** (4,000 characters max):

> First version of Bloomly: watering reminders, 300+ plant types, photo diary, rooms and the leaf scanner.

## Français

**App Store name** (30 characters max):

> Bloomly : soin des plantes

**Google Play name** (30 characters max):

> Bloomly - Arrosage plantes

**App Store subtitle** (30 characters max):

> L'arrosage au bon moment

**Google Play short description** (80 characters max):

> Ne ratez plus un arrosage : rappels malins et conseils pour chaque plante.

**App Store promotional text** (170 characters max, editable without an update):

> Nouveau : photographiez une feuille et Bloomly propose le bon rythme d'arrosage. Bientôt : des plantes partagées pour toute la maison.

**Full description** (4,000 characters max):

> **Bloomly vous dit quand chaque plante a besoin d'eau : aucune n'est oubliée, aucune n'est noyée.**
>
> Ajoutez une plante en dix secondes avec une photo, choisissez son type et la taille du pot, et Bloomly calcule son rythme d'arrosage. Un rappel discret arrive le bon jour, pour la bonne plante.
>
> **UN RYTHME POUR CHAQUE PLANTE**
>
> • Plus de 300 types de plantes, avec leurs besoins en eau, lumière et engrais
> • Taille du pot et saison prises en compte
> • Terre encore humide ? Repoussez le rappel : le rythme s'adapte
>
> **VOTRE JUNGLE EN UN COUP D'ŒIL**
>
> • La liste du jour : arroser, brumiser, nourrir, rempoter
> • Un journal photo par plante pour la voir grandir
> • Des pièces pour regrouper les plantes par fenêtre ou par étage
>
> **SIMPLE ET PRIVÉ**
>
> • Fonctionne sans compte ; connexion avec Apple ou Google seulement pour synchroniser vos appareils
> • Aucune publicité
> • Bloomly Plus (achat unique) débloque les plantes illimitées et le scanner de feuilles
>
> Ajoutez votre première plante et laissez Bloomly s'en souvenir pour vous.

**App Store keywords** (100 characters max, comma-separated, no spaces):

> plante,jardinage,rappel,succulente,orchidée,cactus,fougère,intérieur,botanique,potager,feuille

**Release notes** (4,000 characters max):

> Première version de Bloomly : rappels d'arrosage, plus de 300 types de plantes, journal photo, pièces et scanner de feuilles.

## Categories

| Store | Category | Secondary / subcategories |
| --- | --- | --- |
| App Store | Lifestyle | Utilities |
| Google Play | House & Home | — |

Google Play, tags (5 at most): Gardening, Plants, Reminders, Home, Lifestyle (pick the closest labels Google offers).

## URLs and contact

| Field | Value |
| --- | --- |
| Support URL (Apple, with a contact) | https://bloomly.example/support |
| Marketing URL (Apple, optional) | https://bloomly.example |
| Privacy policy (both stores) | https://bloomly.example/privacy |
| Account deletion (Google Play) | https://bloomly.example/delete-account |
| Terms of use | https://bloomly.example/terms |
| Contact e-mail | hello@bloomly.example |
| Copyright (Apple) | 2026 Bloomly Studio |

## Age

Minimum age in the terms of use: none (general audience).

**Apple, age rating**:

| Question | Answer | Why |
| --- | --- | --- |
| Unrestricted web access | No | Only links to the support and privacy pages. |
| User-generated content | No | Plant photos stay private to the account; nothing is shown to other people. |
| Messaging and chat | No | No contact between users. |
| Advertising | No | No ad SDK in `pubspec.lock`. |
| Every mature theme, violence, gambling | None | Plant care only. |

Expected result: 4+. "Made for Kids": No (not designed for children under 13).

**Google Play, IARC questionnaire** (category: All Other App Types):

| Question | Answer | Why |
| --- | --- | --- |
| Violence, sexuality, language, controlled substances | No | Plant care only. |
| Users interact or exchange content | No | No sharing between accounts. |
| Shares user location | No | No location permission in the merged manifest. |
| Digital purchases | Yes | Bloomly Plus one-time purchase (Play Billing). |
| Unrestricted internet | No | No open browser. |

Expected result: PEGI 3, ESRB Everyone, USK 0.

**Google Play, target audience**: 18+ and 13-17; "appeal to children": No (no child-oriented design or content).

## Privacy

**Apple, App Privacy**:

| Data type | Collected | Linked to user | Tracking | Purpose |
| --- | --- | --- | --- | --- |
| Contact Info > Email Address | Yes (only with Sign in with Apple/Google) | Yes | No | App Functionality |
| Identifiers > User ID | Yes (Firebase Auth) | Yes | No | App Functionality |
| User Content > Photos or Videos | Yes (plant photos synced to Firebase Storage) | Yes | No | App Functionality |
| Purchases > Purchase History | Yes | Yes | No | App Functionality |
| Diagnostics > Crash Data | Yes (Crashlytics) | No | No | App Functionality |

**Google Play, Data safety**:

| Question | Answer |
| --- | --- |
| Collect or share required user data? | Yes |
| Encrypted in transit? | Yes (HTTPS only) |
| Account creation methods | OAuth (Sign in with Apple, Google); the app also works without an account |
| Account deletion link | https://bloomly.example/delete-account |
| Partial data deletion | Yes (delete a plant and its photos in the app) |

| Data | Collected / shared | Ephemeral | Required | Purposes |
| --- | --- | --- | --- | --- |
| Personal info > Email address | Collected, not shared | No | Optional | App functionality, Account management |
| Personal info > User IDs | Collected, not shared | No | Optional | App functionality, Account management |
| Photos and videos > Photos | Collected, not shared | No | Optional | App functionality |
| App info and performance > Crash logs | Collected, not shared | No | Required | App functionality |

## Declarations

| Store | Question | Answer |
| --- | --- | --- |
| Apple | Third-party content rights | Yes: plant illustrations licensed (CC BY), fonts under OFL |
| Apple | Encryption (export) | `ITSAppUsesNonExemptEncryption = false` added to `ios/Runner/Info.plist` |
| Apple | Advertising identifier | No |
| Google | Ads | No |
| Google | App access | All functionality is available without special access |
| Google | News / Government / Health apps | No |
| Google | Financial features | My app doesn't provide any financial features |
| Google | Advertising ID | No (no `AD_ID` permission in the merged manifest) |

## Review

**Apple, notes for the reviewer** (in English):

> Bloomly is a plant watering reminder app.
>
> No login is required: all features work without an account. Sign in with Apple is offered only to sync between devices.
>
> To test on a single device: 1. Tap "Add a plant", take or pick any photo, choose "Monstera". 2. Open the plant and tap "Simulate tomorrow" in Settings > Demo to receive the reminder immediately. 3. Bloomly Plus can be tested with the sandbox account provided by App Store Connect.
>
> Account deletion: Settings > Account > Delete my account.

**App Review contact information**: [first and last name, phone, e-mail to confirm with the publisher].

**Google Play, app access**: All functionality is available without special access.

## Build and testing

**Build and upload** (Flutter):

- iOS: `flutter build ipa` → upload `build/ios/ipa/*.ipa` with Transporter or Xcode Organizer
- Android: `flutter build appbundle` → first upload by hand in Internal testing, then fastlane `supply`

**TestFlight**: internal (the 3 team members); external group "Friends" with "What to Test": "Add three plants, wait for tomorrow's reminders, try the leaf scanner".

**Google Play**: internal (team); closed test with the Google Group bloomly-testers@googlegroups.com, 16 testers, kept for 14 days (personal account created in 2025), feedback to hello@bloomly.example.

**Instructions to testers** (English, French):

> Thanks for testing Bloomly! Add at least three of your real plants, keep the app for two weeks, and tell us when a reminder came too early or too late.
>
> Merci de tester Bloomly ! Ajoutez au moins trois de vos vraies plantes, gardez l'app deux semaines et dites-nous quand un rappel arrive trop tôt ou trop tard.

## Visuals

| File | Size | Where |
| --- | --- | --- |
| `store/<lang>/ios/screenshots-6.9/1-5.png` | 1320 × 2868 | App Store, iPhone 6.9" tab |
| `store/<lang>/android/screenshots/1-5.png` | 1080 × 1920 | Google Play, phone screenshots |
| `store/<lang>/android/feature-graphic-1024x500.png` | 1024 × 500 | Google Play, feature graphic |
| `store/<lang>/ios/header-*.png`, `search-*.png` | 5244 × 2950, 3840 × 1646 | App Store, in-app events and featuring (when requested) |
| `store/android/icon-512.png` | 512 × 512 | Google Play, app icon |

**Screenshots** (same order on both stores):

| # | Screen | Caption (en / fr) |
| --- | --- | --- |
| 1 | Today's list | Never forget to **water** / Plus jamais d'**oubli** |
| 2 | Plant detail with rhythm | A rhythm for **each plant** / Un rythme pour **chaque plante** |
| 3 | Leaf scanner | Snap a **leaf** / Photographiez une **feuille** |
| 4 | Photo diary | Watch them **grow** / Regardez-les **grandir** |
| 5 | Rooms | Your **jungle** at a glance / Votre **jungle** d'un coup d'œil |

## Submission checklist

- [ ] App created in App Store Connect (bundle com.bloomly.app) and in the Play Console (package com.bloomly.app)
- [ ] Texts pasted for English and French
- [ ] Categories, tags, URLs, copyright
- [ ] Apple rating, IARC, target audience
- [ ] Apple privacy and Google data safety
- [ ] Declarations (rights, encryption, ads, access, financial features)
- [ ] Visuals uploaded (6.9", feature graphic, 512 icon)
- [ ] Build uploaded and selected
- [ ] Review notes and contact details
- [ ] Internal test, then closed test started (14-day counter)
- [ ] Manual release chosen for a same-day launch on both stores
