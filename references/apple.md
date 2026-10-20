# App Store Connect, field by field

Current as of October 2026. If the console shows something else, the console is right.

## App information (once, valid for all versions)

| Field | Limit | Advice |
| --- | --- | --- |
| Name | 30 characters | Unique on the App Store. Name alone, or name + short tagline ("PATATE - Pass the bomb"). No stacked keywords. |
| Subtitle | 30 characters | The promise, with the main keyword. Indexed by search. |
| Primary / secondary category | — | Games: up to 2 subcategories. See below. |
| Content rights | — | "Yes, it contains, shows, or accesses third-party content, and I have the necessary rights" as soon as there are licensed third-party sounds, fonts, images or music (CC0, OFL, purchased). "No" only if everything is created by the publisher. |
| Age rating | questionnaire | See below. |
| Privacy policy URL | — | Required. Must also be reachable **inside the app** (guideline 5.1.1). |
| License agreement | — | Keep Apple's standard agreement, unless there are specific terms to link. |

### Categories

Apps: Books, Business, Developer Tools, Education, Entertainment, Finance, Food & Drink, Games, Graphics & Design, Health & Fitness, Kids, Lifestyle, Magazines & Newspapers, Medical, Music, Navigation, News, Photo & Video, Productivity, Reference, Shopping, Social Networking, Sports, Travel, Utilities, Weather.

**Games** subcategories: Action, Adventure, Board, Card, Casino, Casual, Family, Music, Puzzle, Racing, Role Playing, Simulation, Sports, Strategy, Trivia, Word.

Pitfalls: "Family" suggests children (and invites the "Made for Kids" rules); "Board" means board games; "Kids" imposes strict rules (no third-party ads, no external links without parental gate).

## Version page (every version)

| Field | Limit | Advice |
| --- | --- | --- |
| Promotional text | 170 characters | Editable without a new version: announcements, news, events. Not indexed. |
| Description | 4,000 characters | No emoji (rejected), no prices, no competitor names. First sentence = the hook. Not indexed by Apple search. |
| Keywords | 100 characters | Commas **without spaces**. Do not repeat the name, the subtitle, the category, or generic "app" / "game" unless useful. No third-party brands. |
| What's New in This Version | 4,000 characters | Not for the very first version. |
| Support URL | — | Required. The page must offer a **way to make contact** (e-mail or form). |
| Marketing URL | — | Optional. |
| Copyright | — | "2026 Publisher Name". |
| Screenshots and app previews | — | See references/visuals.md. |
| Build | — | Uploaded with Xcode, Transporter, fastlane, `eas submit` or CI (references/frameworks.md). |
| Sign-in information | — | Demo account if the app requires sign-in. "Sign-in required: no" if there is an automatic anonymous account. |
| Review notes | 4,000 characters | In English. See below. |
| App Review contact information | — | First name, last name, phone, e-mail reachable during review. |
| Version release | — | "Manually" to choose the release day (recommended for a first release coordinated with Google); "Automatically"; or phased release over 7 days. |

## Age rating (questionnaire, 4+ / 9+ / 13+ / 16+ / 18+ system)

For each theme, answer None / Infrequent or Mild / Frequent or Intense, or Yes / No.

| Group | Questions | How to answer |
| --- | --- | --- |
| In-app features | Unrestricted web access (open in-app browser), user-generated content, messaging and chat, advertising | A username visible to others is user-generated content (limited); open chat is "messaging and chat". A link to a specific website is not unrestricted web access. |
| Mature themes | Profanity or crude humor, horror or fear themes, alcohol / tobacco / drugs, mature or suggestive themes | "Infrequent or Mild" as soon as there is any, even light. |
| Medical or wellness | Medical information, treatment | Only if the app covers it. |
| Sexuality or nudity | — | — |
| Violence | Cartoon or fantasy, realistic, prolonged or graphic, guns | A cartoon explosion is "cartoon or fantasy violence, infrequent or mild". |
| Chance-based activities | Simulated gambling, contests, loot boxes | A random draw with no stake and no prize is not gambling. |
| Controls | Parental controls, age assurance | Only if the app has them. |

"Made for Kids": do not tick unless the app is designed for children under 13 (very strict rules).

## App Privacy ("privacy nutrition labels")

1. "Do you or your third-party partners collect data from this app?": yes as soon as any data leaves the phone and is stored (even an anonymous identifier). Data processed only on the device does not count.
2. For each data type collected: purposes, linked to the user's identity or not, used for tracking or not.

Data types: Contact Info (name, e-mail, phone, physical address, other) · Health & Fitness · Financial Info · Location (precise, coarse) · Sensitive Info · Contacts · User Content (e-mails or text messages, photos or videos, audio, gameplay content, customer support, other user content) · Browsing History · Search History · Identifiers (user ID, device ID) · Purchases · Usage Data (product interaction, advertising data, other) · Diagnostics (crash data, performance data, other) · Surroundings · Body · Other Data.

Purposes: Third-Party Advertising · Developer's Advertising or Marketing · Analytics · Product Personalization · App Functionality · Other Purposes.

Guidelines:
- Account identifier (even anonymous, Firebase for example): Identifiers > User ID, linked, App Functionality.
- Username: User Content > Other User Content (or Contact Info > Name if it is a real name).
- Games, scores, game actions: User Content > Gameplay Content.
- Push notification token: usually not declared (it is not a device ID in Apple's sense); declare it under Identifiers > Device ID only if it is used for anything other than sending notifications.
- Analytics or crash SDKs (Crashlytics, Sentry, Analytics): declare them (Diagnostics, Usage Data).
- **Tracking**: only if data is combined with other companies' data for targeted advertising or shared with data brokers; in that case, App Tracking Transparency is required.

## Other declarations

| Question | Usual answer |
| --- | --- |
| Encryption compliance (export) | With `ITSAppUsesNonExemptEncryption = false` in the app's Info.plist (where to set it per technology: references/frameworks.md), the question no longer comes up. Correct if the app only uses HTTPS and the system's encryption. |
| Advertising identifier (IDFA) | No, unless there is an ad or attribution SDK. |
| Third-party content | See "Content rights". |
| Pricing and availability | Free, chosen countries; for a French-only release, all countries remain possible. |

## Guidelines that most often cause rejection

- **2.1**: the reviewer cannot test (sign-in impossible, empty app without other players) → demo account, solo mode, video.
- **5.1.1(v)**: account creation without **account deletion inside the app** → say where it is in the notes.
- **4.8**: Google or Facebook sign-in without **Sign in with Apple**.
- **1.2**: user-generated content without filtering, reporting and blocking.
- **2.3**: description, screenshots or keywords that promise missing features, or third-party brand keywords.
- **5.1.2**: undeclared data collection, or no privacy policy inside the app.
- **3.1.1**: digital purchases outside Apple's system.

## Notes for the reviewer (template, in English)

> [App] is [what the app does in one sentence].
>
> [Sign-in: "No login is required: the app creates an anonymous account on first launch." or demo account credentials.]
>
> To test on a single device: [numbered steps: solo mode, demo group with code, prefilled data].
>
> [If multiplayer: code of a demo group with bots, and/or link to a video of a full game.]
>
> Account deletion: [exact path in the app].
> [Blocking / reporting: exact path, if there is content between users.]

## TestFlight

- **Internal testing**: up to 100 App Store Connect team members, **no review**, available a few minutes after the build is processed.
- **External testing**: up to 10,000 testers by e-mail or public link, after **Beta App Review** (usually under 24 h). To fill in: beta description, feedback e-mail, marketing URL, privacy URL, "What to Test", sign-in information.
- A TestFlight build expires after 90 days.

## Uploading a build

Build an archive with the app's technology, then upload it with Xcode Organizer, Transporter, `xcrun altool`, fastlane, `eas submit` or a CI service: commands per technology in references/frameworks.md. After processing (a few minutes to an hour), the build appears in TestFlight and can be selected on the version page.
