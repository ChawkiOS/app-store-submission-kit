# Google Play Console, field by field

Current as of October 2026. Labels are given in English (the console's most common language). If the console shows something else, the console is right.

## Main store listing

| Field | Limit | Advice |
| --- | --- | --- |
| App name | 30 characters | May include a tagline ("PATATE - Pass the bomb"); good for search. No emoji, no "best", "free", "#1". |
| Short description | 80 characters | Indexed. The promise + the main keyword. |
| Full description | 4,000 characters | Indexed by Google: repeat important words naturally, no stuffing. No made-up testimonials or rankings. |
| App icon | 512 × 512, PNG or JPEG, 1 MB max | No rounded corners or shadow (Google applies them). |
| Feature graphic | 1024 × 500, PNG or JPEG, 15 MB max | Required. Keep important text away from the edges. |
| Phone screenshots | 2 to 8 | See references/visuals.md. |
| Tablet screenshots | — | Only if the app targets tablets. |
| Video | YouTube URL | Optional. |
| Contact details | — | E-mail required (public), website, phone optional. |

### Categories and tags

Games: Action, Adventure, Arcade, Board, Card, Casino, Casual, Educational, Music, Puzzle, Racing, Role Playing, Simulation, Sports, Strategy, Trivia, Word. In some console languages "Casual" does not always appear: pick "Arcade" for reflex mini-games.

Apps: Art & Design, Auto & Vehicles, Beauty, Books & Reference, Business, Comics, Communication, Dating, Education, Entertainment, Events, Finance, Food & Drink, Health & Fitness, House & Home, Libraries & Demo, Lifestyle, Maps & Navigation, Medical, Music & Audio, News & Magazines, Parenting, Personalization, Photography, Productivity, Shopping, Social, Sports, Tools, Travel & Local, Video Players & Editors, Weather.

Tags: **5 at most**, chosen from Google's list (Store settings). Only pick those that truly describe the app ("Offline" only if the app works without Internet, "Local multiplayer" only on a single device).

## App content

| Section | Usual answer |
| --- | --- |
| Privacy policy | Policy URL. |
| Ads | "No" if there is no ad SDK, including no house ads paid for by a third party. |
| App access | "All functionality is available without special access" if there is no login or an automatic anonymous account; otherwise provide test credentials. Add an instruction if the app needs several players. |
| Content rating | IARC questionnaire (below). |
| Target audience and content | Target age groups; see below. |
| News apps | No (unless it is a news app). |
| Data safety | Form below. |
| Government apps | No. |
| Financial features | "My app doesn't provide any financial features" unless banking, loans, crypto, peer-to-peer payments. Google Play in-app purchases are not "financial features". |
| Health apps | No health features (unless it is a health app). |
| Advertising ID | No, unless there is an ad or attribution SDK. If the console says the `AD_ID` permission is in the build, remove it from the manifest (how per technology: references/frameworks.md) or answer yes with the reason. |
| Sensitive permissions | Photos and videos, background location, foreground services, exact alarms, full-screen intents: declarations to fill in if present. Better: block those added by libraries and not used, then check the final manifest. |

### Target audience and content

- Tick the age groups actually targeted. **Do not tick any group under 13** unless the app is designed for children: otherwise the Families program applies (certified SDKs, no personalized ads, suitable content).
- "Could your app unintentionally appeal to children?": No if the app is not made for them (minimum age in the terms, social mechanics, notifications), even with a cartoon style; Google may ask for a justification.

## IARC questionnaire (Content rating), step by step

First choose the category (Game, or Social / Communication / Reference… for an app). Then, for a game:

| Question | How to answer |
| --- | --- |
| Violence, Blood, or Gory Images | **Yes** as soon as there is any violence, even cartoon, including against the player's character ("You blew up"). The following questions make clear it is mild. |
| Select all that the game includes | Against humans / against non-humans (animals, imaginary creatures, robots, vehicles) / disturbing images without a violent act / blood outside a violent act. An object character (potato, bomb) is an imaginary creature. |
| Setting | Fantastical (drawn world, unrealistic characters) or Realistic. |
| Pixelated or childlike style | Yes for a simple cartoon style, thick outlines, characters with exaggerated features. Does not change the target audience. |
| Reactions to violence | Unrealistic if nobody suffers or reacts realistically. |
| How is this violence presented | Referred to / rarely or often depicted from a distant or close-up perspective. A full-screen explosion once per round: "Rarely depicted from a close-up perspective". |
| Level of blood and/or gore | None, Mild, Moderate, High. |
| Do any of these creatures behave or respond like humans | No if there is no pain, fear or realistic human reaction. |
| Violence against real-world animals | No unless real animals. |
| Fierce sounds, sinister or intimidating characters, dark overtones | No for a light tone and cartoon sounds. |
| Fear | "Scary, horrifying, or disturbing": No unless horror, monsters, anxious atmosphere. |
| Sexuality, Language, Controlled substances, Crude humor | Depending on actual content; light dares or jokes are not "crude humor" if they are neither scatological nor sexual. |
| Gambling | No if there is no money wagered and no reward with real value. |
| Users interact or exchange content | Yes if usernames or user content are visible to others. Specify: no chat if that is the case. |
| Shares user location | Only if the app shares location. |
| Digital purchases | Yes if there are in-app purchases. |
| Miscellaneous / Unrestricted internet | No if there is no open browser. |

Expected result for mild cartoon violence: PEGI 3 or 7, ESRB Everyone or E10+, USK 0 or 6.

## Data safety

1. Does your app collect or share any of the required user data types? → Yes as soon as any data is sent and stored.
2. Is all of the user data collected by your app encrypted in transit? → Yes if everything goes over HTTPS.
3. Account creation methods → Username and password / Username and other authentication / OAuth / **Other** (anonymous account created automatically: describe it) / My app does not allow users to create an account.
4. Account deletion link → URL of a web page that explains how to delete the account **and** how to request it without the app.
5. Partial data deletion without deleting the account → Yes only if the app really allows it.
6. For each type collected: Collected / Shared (service providers processing on your behalf, such as Firebase, Supabase or your hosting, are not sharing), processed ephemerally (usually No), required or optional, purposes.

Types: Location (approximate, precise) · Personal info (Name, Email address, User IDs, Address, Phone number, Race and ethnicity, Political or religious beliefs, Sexual orientation, Other info) · Financial info · Health and fitness · Messages (Emails, SMS or MMS, Other in-app messages) · Photos and videos · Audio files · Files and docs · Calendar · Contacts · App activity (App interactions, In-app search history, Installed apps, Other user-generated content, Other actions) · Web browsing · App info and performance (Crash logs, Diagnostics, Other app performance data) · Device or other IDs.

Purposes: App functionality · Analytics · Developer communications · Advertising or marketing · Fraud prevention, security, and compliance · Personalization · Account management.

Guidelines: username = Personal info > Name; account identifier = User IDs (App functionality, Account management); game actions = App interactions; push token = Device or other IDs (optional if the user can decline notifications); sensors processed on the device: nothing to declare.

## Testing and release

| Step | Details |
| --- | --- |
| First upload | **By hand**: Test and release > Testing > Internal testing > Create release, upload the `.aab` (how to build it per technology: references/frameworks.md). Later uploads can go through the API (fastlane `supply`, Gradle Play Publisher, `eas submit`, CI). |
| Play App Signing | Accept: Google signs the final app. SHA-256 fingerprint: Test and release > App integrity (or "Protected with Play" > Play Store protection > Play app signing; direct URL `…/app/<id>/keymanagement`). Put it in `.well-known/assetlinks.json` for App Links. |
| Internal testing | Up to 100 testers by e-mail, no review, available within minutes. |
| Closed testing | E-mail list or Google Group, first version reviewed by Google (hours to days). **Personal account created after November 13, 2023: at least 12 testers opted in for 14 consecutive days** before you can apply for production access. Aim for 15 to 18 testers. |
| Production access | Questionnaire about the closed test (how testers were recruited, feedback received, changes made, release readiness). Google answers within a few days. |
| Feedback | E-mail address or URL for tester feedback. |

### Automatic upload (fastlane, Gradle Play Publisher, EAS, CI)

Every automated upload tool uses the Play Developer API and requires a Google service account key:
1. Google Cloud Console: create a service account (no Cloud role), JSON key.
2. Enable the **Google Play Android Developer API** on that account's Cloud project (otherwise error 403 "has not been used in project …").
3. Play Console > Users and permissions: invite the service account's address, grant access to the app with "Release apps to testing tracks" and "Manage testing tracks" (otherwise error "The Google service account cannot submit this app"). Wait a few minutes.
4. Keep the JSON key out of the project (password manager): it can publish on the account.
