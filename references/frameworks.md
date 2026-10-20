# Mobile technologies: where to find the facts, how to build and upload

The listings and questionnaires are the same whatever the app is built with; only the places to read facts from and the build commands differ. Detect the technology first (step 2 of SKILL.md), then use its row below. If the project uses something not listed, look for the same facts in its equivalent files, and in the **final** build outputs (the built `Info.plist` and merged `AndroidManifest.xml`), which are the truth for every technology.

## Detecting the technology

| Sign in the project | Technology |
| --- | --- |
| `*.xcodeproj` / `*.xcworkspace` only, Swift or Objective-C sources | Native iOS (Swift, SwiftUI, UIKit) |
| `settings.gradle(.kts)` + `app/build.gradle(.kts)` only, Kotlin or Java sources | Native Android (Kotlin, Jetpack Compose, Java) |
| `app.json` / `app.config.*` with an `expo` key, `expo` in `package.json` | Expo (React Native) |
| `react-native` in `package.json`, `ios/` and `android/` folders, no Expo config | React Native CLI (bare) |
| `pubspec.yaml` with `flutter:` | Flutter |
| `composeApp/` or `shared/` with `kotlin("multiplatform")`, plus `iosApp/` | Kotlin Multiplatform / Compose Multiplatform |
| `capacitor.config.*` | Ionic / Capacitor |
| `config.xml` with `<widget>` | Apache Cordova |
| `nativescript.config.*` | NativeScript |
| `*.csproj` with `<UseMaui>true</UseMaui>` or `-ios` / `-android` target frameworks | .NET MAUI |
| `ProjectSettings/ProjectSettings.asset`, `Assets/` | Unity |
| `project.godot`, `export_presets.cfg` | Godot |

## Where the facts are

| Technology | Name, IDs, version | Native config | Translations | Icon, theme |
| --- | --- | --- | --- | --- |
| Native iOS | Target build settings: `PRODUCT_BUNDLE_IDENTIFIER`, `MARKETING_VERSION`, `CURRENT_PROJECT_VERSION`, display name (`project.pbxproj`) | `Info.plist`, `*.entitlements`, `PrivacyInfo.xcprivacy` | `Localizable.xcstrings`, `*.lproj/Localizable.strings` | `Assets.xcassets/AppIcon.appiconset`, `AccentColor` |
| Native Android | `app/build.gradle(.kts)`: `applicationId`, `versionName`, `versionCode`; `app_name` in `strings.xml` | `app/src/main/AndroidManifest.xml` | `res/values-<lang>/strings.xml` | `res/mipmap-*`, `res/values/colors.xml`, `themes.xml` |
| Expo | `app.json` / `app.config.*`: `name`, `ios.bundleIdentifier`, `android.package`, `version` | `ios.infoPlist`, `android.permissions`, `plugins`; `ios/` and `android/` if prebuilt | i18n files (`locales/`, `i18n/`), `expo-localization` | `icon`, `ios.icon`, `android.adaptiveIcon`, theme files |
| React Native CLI | `package.json`, `ios/<App>/Info.plist`, `android/app/build.gradle` | `ios/<App>/Info.plist`, `android/app/src/main/AndroidManifest.xml` | i18n files (`locales/`, `i18n/`) | `ios/<App>/Images.xcassets`, `android/app/src/main/res` |
| Flutter | `pubspec.yaml` (`version: x.y.z+build`), `ios/Runner.xcodeproj`, `android/app/build.gradle(.kts)` | `ios/Runner/Info.plist`, `android/app/src/main/AndroidManifest.xml` | `lib/l10n/*.arb`, `l10n.yaml` | `flutter_launcher_icons` config, `ThemeData` in `lib/` |
| Kotlin / Compose Multiplatform | `composeApp/build.gradle(.kts)`, `iosApp/` Xcode project | `iosApp/iosApp/Info.plist`, `composeApp/src/androidMain/AndroidManifest.xml` | `composeResources/values-<lang>/strings.xml` | `composeResources/drawable`, Material theme |
| Ionic / Capacitor | `capacitor.config.*` (`appId`, `appName`), `package.json` | `ios/App/App/Info.plist`, `android/app/src/main/AndroidManifest.xml` | web i18n files (`assets/i18n/`) | `resources/` (`@capacitor/assets`), CSS variables |
| Cordova | `config.xml` (`id`, `version`, `<name>`) | `config.xml` (`<edit-config>`, `<config-file>`), `platforms/` | web i18n files | `<icon>` in `config.xml`, CSS |
| NativeScript | `nativescript.config.*` (`id`), `package.json` | `App_Resources/iOS/Info.plist`, `App_Resources/Android/src/main/AndroidManifest.xml` | `i18n/` | `App_Resources/` |
| .NET MAUI | `.csproj`: `ApplicationId`, `ApplicationTitle`, `ApplicationDisplayVersion`, `ApplicationVersion` | `Platforms/iOS/Info.plist`, `Platforms/Android/AndroidManifest.xml` | `Resources/Strings/*.resx` | `Resources/AppIcon`, `Resources/Styles/Colors.xaml` |
| Unity | Player Settings (`ProjectSettings.asset`): `productName`, `applicationIdentifier`, `bundleVersion` | Player Settings, `Assets/Plugins/Android/AndroidManifest.xml`, generated Xcode project | Localization package tables | Player Settings icons |
| Godot | `export_presets.cfg` (`package/unique_name`, `version/name`, `bundle_identifier`) | export presets, `android/build/` if custom build | `*.translation`, `*.csv`, `*.po` | `project.godot` icon |

Also, for every technology:
- **Dependencies** answer most questionnaires: `Podfile.lock` / `Package.resolved` (iOS), Gradle dependencies, `package.json`, `pubspec.lock`, `*.csproj` packages, Unity `Packages/manifest.json`. Look for ad SDKs (AdMob, AppLovin, Unity Ads), attribution (Adjust, AppsFlyer, Branch), analytics and crash reporting (Firebase, Sentry, Amplitude, Mixpanel), payments (StoreKit, Play Billing, RevenueCat), authentication (Sign in with Apple, Google Sign-In, Firebase Auth, Supabase, Auth0).
- **Privacy manifests** (`PrivacyInfo.xcprivacy`, in the app and inside each SDK) list collected data types and tracking domains: a good starting point for Apple App Privacy.
- **Final permissions**: libraries add permissions at build time. Check the built app, not only the source: Android merged manifest (`app/build/intermediates/merged_manifests/release/…/AndroidManifest.xml`, or the APK Analyzer in Android Studio), and the `Info.plist` of the built `.app`.

## Common settings, per technology

| Setting | Where |
| --- | --- |
| `ITSAppUsesNonExemptEncryption = false` (skips the export compliance question) | In the iOS `Info.plist` listed above; Expo: `ios.infoPlist`; Cordova: `<edit-config>` in `config.xml`; Unity: post-build script or Xcode project. |
| Remove the `AD_ID` permission added by a library (Android) | `<uses-permission android:name="com.google.android.gms.permission.AD_ID" tools:node="remove" />` in the app's `AndroidManifest.xml` (with `xmlns:tools`); Expo: `android.blockedPermissions`; Unity: custom main manifest. The same trick removes any other unused permission. |
| iPad support (decides whether iPad screenshots are required) | Native iOS / Flutter / React Native / KMP / Capacitor: `TARGETED_DEVICE_FAMILY` in Xcode (`1` = iPhone, `1,2` = iPhone and iPad); Expo: `ios.supportsTablet`; .NET MAUI: `UIDeviceFamily` in `Info.plist`; Unity: Player Settings > Target Device. |
| App icon 1024 × 1024 for Apple | Comes from the build's asset catalog (or the framework's icon setting above). |

## Building and uploading

### iOS (App Store Connect)

Every technology ends with an Xcode archive (`.ipa`) signed with a distribution certificate.

| Technology | Build |
| --- | --- |
| Native iOS, React Native CLI, KMP, Capacitor, NativeScript, Unity, Godot | Open the (generated) Xcode project or workspace > Product > Archive. Capacitor: `npx cap sync ios` first; Unity / Godot: export the Xcode project first; NativeScript: `ns build ios --release --for-device`. |
| Flutter | `flutter build ipa` (then upload the `.ipa` from `build/ios/ipa/`). |
| Expo | `npx eas-cli@latest build --platform ios --profile production`. |
| Cordova | `cordova build ios --release --device`. |
| .NET MAUI | `dotnet publish -f net<version>-ios -c Release` (with signing properties). |

Upload, any technology: Xcode Organizer (Distribute App > App Store Connect), the **Transporter** app, `xcrun altool --upload-app`, **fastlane** (`deliver`, `pilot` for TestFlight), `eas submit` (Expo), or a CI service (Xcode Cloud, Codemagic, Bitrise, GitHub Actions). Xcode, fastlane and EAS can manage certificates and provisioning profiles; capabilities (Push, Associated Domains, Sign in with Apple) must match the app's entitlements.

### Android (Play Console)

Google Play requires an **Android App Bundle** (`.aab`), signed with an upload key (Play App Signing then signs the final app).

| Technology | Build |
| --- | --- |
| Native Android, React Native CLI, KMP, Capacitor | `./gradlew bundleRelease` (in `android/` for React Native and Capacitor; Capacitor: `npx cap sync android` first), or Android Studio > Build > Generate Signed App Bundle. |
| Flutter | `flutter build appbundle`. |
| Expo | `npx eas-cli@latest build --platform android --profile production`. |
| Cordova | `cordova build android --release -- --packageType=bundle`. |
| NativeScript | `ns build android --release --aab` (with keystore options). |
| .NET MAUI | `dotnet publish -f net<version>-android -c Release` (AAB by default, with signing properties). |
| Unity | Build Settings > Android > Build App Bundle (Google Play). |
| Godot | Export > Android, Gradle build enabled, export format AAB. |

Upload: the **first** upload is always by hand in the Play Console (see references/google.md). Later uploads can be automated with the Play Developer API through **fastlane** (`supply`), the **Gradle Play Publisher** plugin, `eas submit` (Expo) or a CI service; all of them need the same Google service account key (references/google.md).
