# Store visuals

Current as of October 2026. Check in the console: when a size is rejected, the error message lists the accepted sizes.

## Apple

| Visual | Size | Notes |
| --- | --- | --- |
| Icon | 1024 × 1024, no transparency or rounded corners | Provided by the build (asset catalog or the framework's icon setting, references/frameworks.md). |
| iPhone 6.9" screenshots (required) | 1320 × 2868 (or 1290 × 2796) | Up to 10. Apple reuses them for smaller screens: upload in the **6.9"** tab. |
| iPhone 6.1" / 6.3" screenshots (if requested) | 1206 × 2622 (or 1179 × 2556) | Only if the console insists. |
| iPad 13" screenshots | 2064 × 2752 | Required only if the app runs on iPad (device family, references/frameworks.md). |
| App preview video | 886 × 1920 or 1920 × 886, 15 to 30 s | Optional. App footage only. |
| Header / featuring | 5244 × 2950 and 3840 × 1646 | Requested for in-app events and featuring. Subject centered, nothing important near the edges. |
| Search results | 5244 × 2950 | Same rule. |

## Google Play

| Visual | Size | Notes |
| --- | --- | --- |
| Icon | 512 × 512, PNG or JPEG, 1 MB max | Google applies the shape and shadow. |
| Feature graphic | 1024 × 500, 15 MB max | Required. |
| Phone screenshots | 2 to 8, sides between 320 and 3840 px, 2:1 ratio max | 1080 × 1920 (9:16) recommended; at least 4 at 1080 px to be eligible for featuring. |
| 7" and 10" tablet screenshots | — | Only if the app targets tablets. |

## Screenshots: what to show

- 4 to 6 screenshots, in the order of the journey that makes people want the app: the strongest moment first (not the login screen).
- A short caption at the top of each screenshot (4 to 6 words), one highlighted word, one explanatory sentence at most.
- **Real screens** of the app, in a phone frame; the same visuals serve both stores, at the right sizes.
- No misleading fake content, no prices, no "#1" badges, no Apple or Google logos, no real usernames of friends or family (use demo accounts).
- One set per listing language: captions and app displayed in the listing's language.

## Producing the visuals

With the skill's script (see SKILL.md, step 4): `visuals.json` describes the brand and the screenshots for each language, `scripts/render_visuals.py` renders everything at the right sizes with headless Chrome, and one contact sheet per language lets you check everything at once.

Good to know:
- Take the raw screens during a demo session, **after** animations have finished, whatever the app is built with:
  - on a real phone (iPhone 6.9": 1320 × 2868 native);
  - in the iOS Simulator on a 6.9" iPhone (iPhone 16 Pro Max or newer): `xcrun simctl io booted screenshot screen.png`; `xcrun simctl status_bar booted override --time 9:41 --batteryLevel 100` for a clean status bar;
  - on an Android device or emulator: `adb exec-out screencap -p > screen.png`; demo mode for a clean status bar: `adb shell settings put global sysui_demo_allowed 1`, then the `com.android.systemui.demo` broadcasts;
  - automatically in each language with fastlane `snapshot` (iOS) / `screengrab` (Android), Flutter `integration_test`, Maestro or Detox.
- Headless Chrome enforces a window at least 500 px wide: to see a page at phone width, put it in a 375 px `iframe`.
- The script checks the size of every file it renders (on macOS, `sips -g pixelWidth -g pixelHeight` checks any other image).
- Layout: `store/<lang>/ios/`, `store/<lang>/android/`, `store/android/icon-512.png`, `store/raw-screens/<lang>/`, `visuals.json` at the root.
