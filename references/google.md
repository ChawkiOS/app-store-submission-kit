# Google Play Console, champ par champ

À jour d'octobre 2026. Les libellés sont donnés en anglais (langue la plus courante de la console) avec le français entre parenthèses quand il est utile. Si la console affiche autre chose, elle a raison.

## Fiche principale (Store listing)

| Champ | Limite | Conseils |
| --- | --- | --- |
| App name | 30 caractères | Peut contenir une accroche (« PATATE - Passe la bombe ») ; bon pour la recherche. Pas d'emoji, pas de « meilleur », « gratuit », « n°1 ». |
| Short description | 80 caractères | Indexée. La promesse + le mot-clé principal. |
| Full description | 4 000 caractères | Indexée par Google : répéter naturellement les mots importants, sans bourrage. Pas de témoignages inventés ni de classements. |
| App icon | 512 × 512, PNG ou JPEG, 1 Mo max | Sans coins arrondis ni ombre (Google les applique). |
| Feature graphic | 1024 × 500, PNG ou JPEG, 15 Mo max | Obligatoire. Texte important loin des bords. |
| Phone screenshots | 2 à 8 | Voir references/visuels.md. |
| Tablet screenshots | — | Seulement si l'app vise les tablettes. |
| Video | URL YouTube | Facultative. |
| Contact details | — | E-mail obligatoire (public), site web, téléphone facultatif. |

### Catégories et tags

Jeux : Action, Adventure, Arcade, Board (jeux de plateau), Card, Casino, Casual, Educational, Music, Puzzle, Racing, Role Playing, Simulation, Sports, Strategy, Trivia, Word. Dans la console en français, « Casual » n'apparaît pas toujours : prendre « Arcade » pour des mini-jeux de réflexe.

Apps : Art & Design, Auto & Vehicles, Beauty, Books & Reference, Business, Comics, Communication, Dating, Education, Entertainment, Events, Finance, Food & Drink, Health & Fitness, House & Home, Libraries & Demo, Lifestyle, Maps & Navigation, Medical, Music & Audio, News & Magazines, Parenting, Personalization, Photography, Productivity, Shopping, Social, Sports, Tools, Travel & Local, Video Players & Editors, Weather.

Tags : **5 au plus**, choisis dans la liste de Google (Store settings). Ne prendre que ceux qui décrivent vraiment l'app (« Offline » seulement si l'app marche sans Internet, « Local multiplayer » seulement sur un même appareil).

## App content (Contenu de l'app)

| Section | Réponse habituelle |
| --- | --- |
| Privacy policy | URL de la politique. |
| Ads | « No » si aucun SDK publicitaire, y compris pas de pub maison payée par un tiers. |
| App access | « All functionality is available without special access » si pas de connexion ou compte anonyme automatique ; sinon fournir des identifiants de test. Ajouter une instruction si l'app a besoin de plusieurs joueurs. |
| Content rating | Questionnaire IARC (plus bas). |
| Target audience and content | Tranches d'âge visées ; voir plus bas. |
| News apps | No (sauf app d'actualité). |
| Data safety | Formulaire plus bas. |
| Government apps | No. |
| Financial features | « My app doesn't provide any financial features » sauf banque, prêt, crypto, paiement entre personnes. Les achats intégrés Google Play ne sont pas des « financial features ». |
| Health apps | No health features (sauf app de santé). |
| Advertising ID | No, sauf SDK pub ou attribution. Si la console dit que la permission `AD_ID` est dans le build, la bloquer (Expo : `android.blockedPermissions`) ou répondre oui avec la raison. |
| Permissions sensibles | Photos et vidéos, localisation en arrière-plan, services au premier plan, alarmes exactes, intentions plein écran : déclarations à remplir si présentes. Mieux : bloquer celles ajoutées par des bibliothèques et non utilisées, puis vérifier le manifeste final. |

### Public cible (Target audience and content)

- Cocher les tranches réellement visées. **Ne pas cocher de tranche de moins de 13 ans** sauf app conçue pour les enfants : sinon le programme Familles s'applique (SDK certifiés, pas de pub personnalisée, contenus adaptés).
- « Could your app unintentionally appeal to children? » : No si l'app n'est pas faite pour eux (âge minimum dans les CGU, mécaniques sociales, notifications), même avec un style cartoon ; Google peut demander une justification.

## Questionnaire IARC (Content rating), pas à pas

Choisir d'abord la catégorie (Game, ou Social / Communication / Reference… pour une app). Puis, pour un jeu :

| Question | Comment répondre |
| --- | --- |
| Violence, Blood, or Gory Images | **Yes** dès qu'il y a une violence, même de dessin animé, y compris contre le personnage du joueur (« Tu as explosé »). Les questions suivantes précisent qu'elle est légère. |
| Select all that the game includes | Contre des humains / contre des non-humains (animaux, créatures imaginaires, robots, véhicules) / images dérangeantes sans acte violent / sang hors acte violent. Un personnage objet (patate, bombe) est une créature imaginaire. |
| Setting | Fantastical (monde dessiné, personnages non réalistes) ou Realistic. |
| Pixelated or childlike style | Yes pour un style cartoon simple, contours épais, personnages aux traits exagérés. Ne change pas le public cible. |
| Reactions to violence | Unrealistic si personne ne souffre ni ne réagit de façon réaliste. |
| How is this violence presented | Referred to / rarely or often depicted from a distant or close-up perspective. Une explosion plein écran une fois par manche : « Rarely depicted from a close-up perspective ». |
| Level of blood and/or gore | None, Mild, Moderate, High. |
| Do any of these creatures behave or respond like humans | No si pas de douleur, de peur ni de réaction humaine réaliste. |
| Violence against real-world animals | No sauf animaux réels. |
| Fierce sounds, sinister or intimidating characters, dark overtones | No pour un ton léger et des sons cartoon. |
| Fear | « Scary, horrifying, or disturbing » : No sauf horreur, monstres, ambiance angoissante. |
| Sexuality, Language, Controlled substances, Crude humor | Selon le contenu réel ; les gages ou blagues légères ne sont pas de l'« humour cru » s'ils ne sont ni scatologiques ni sexuels. |
| Gambling | No si aucune mise d'argent ni récompense ayant une valeur. |
| Users interact or exchange content | Yes si des pseudos ou contenus d'utilisateurs sont visibles par d'autres. Préciser : pas de chat si c'est le cas. |
| Shares user location | Seulement si l'app partage la position. |
| Digital purchases | Yes s'il y a des achats intégrés. |
| Miscellaneous / Unrestricted internet | No si pas de navigateur libre. |

Résultat attendu pour une violence cartoon légère : PEGI 3 ou 7, ESRB Everyone ou E10+, USK 0 ou 6.

## Sécurité des données (Data safety)

1. Does your app collect or share any of the required user data types? → Yes dès qu'une donnée est envoyée et gardée.
2. Is all of the user data collected by your app encrypted in transit? → Yes si tout passe en HTTPS.
3. Account creation methods → Username and password / Username and other authentication / OAuth / **Other** (compte anonyme créé automatiquement : le décrire) / My app does not allow users to create an account.
4. Lien de suppression du compte → URL d'une page web qui explique comment supprimer le compte **et** comment le demander sans l'app.
5. Suppression partielle des données sans supprimer le compte → Yes seulement si l'app le permet vraiment.
6. Pour chaque type collecté : Collected / Shared (les prestataires qui traitent pour vous, comme Firebase ou Expo, ne sont pas du partage), processed ephemerally (No en général), required or optional, purposes.

Types : Location (approximate, precise) · Personal info (Name, Email address, User IDs, Address, Phone number, Race and ethnicity, Political or religious beliefs, Sexual orientation, Other info) · Financial info · Health and fitness · Messages (Emails, SMS or MMS, Other in-app messages) · Photos and videos · Audio files · Files and docs · Calendar · Contacts · App activity (App interactions, In-app search history, Installed apps, Other user-generated content, Other actions) · Web browsing · App info and performance (Crash logs, Diagnostics, Other app performance data) · Device or other IDs.

Finalités : App functionality · Analytics · Developer communications · Advertising or marketing · Fraud prevention, security, and compliance · Personalization · Account management.

Repères : pseudo = Personal info > Name ; identifiant de compte = User IDs (App functionality, Account management) ; actions de jeu = App interactions ; jeton push = Device or other IDs (optional si l'utilisateur peut refuser les notifications) ; capteurs traités sur l'appareil : rien à déclarer.

## Tests et sortie

| Étape | Détail |
| --- | --- |
| Premier envoi | **À la main** : Test and release > Testing > Internal testing > Create release, déposer le `.aab`. Les envois suivants peuvent passer par l'API (`eas submit`). |
| Play App Signing | Accepter : Google signe l'app finale. Empreinte SHA-256 : Test and release > App integrity (ou « Protected with Play » > Play Store protection > Play app signing ; adresse directe `…/app/<id>/keymanagement`). À mettre dans `.well-known/assetlinks.json` pour les App Links. |
| Internal testing | Jusqu'à 100 testeurs par e-mail, sans review, disponible en quelques minutes. |
| Closed testing | Liste d'e-mails ou Google Group, première version relue par Google (heures à jours). **Compte personnel créé après le 13 novembre 2023 : au moins 12 testeurs inscrits pendant 14 jours d'affilée** avant de pouvoir demander l'accès à la production. Viser 15 à 18 testeurs. |
| Production access | Questionnaire sur le test fermé (comment les testeurs ont été recrutés, retours reçus, changements faits, préparation à la sortie). Réponse de Google en quelques jours. |
| Feedback | Adresse e-mail ou URL pour les retours des testeurs. |

### Envoi automatique avec EAS

```bash
npx eas-cli@latest build --platform android --profile production
npx eas-cli@latest submit --platform android --latest
```

Demande une clé de compte de service Google :
1. Google Cloud Console : créer un compte de service (aucun rôle Cloud), clé JSON.
2. Activer **Google Play Android Developer API** sur le projet Cloud de ce compte (erreur 403 « has not been used in project … » sinon).
3. Play Console > Users and permissions : inviter l'adresse du compte de service, donner l'accès à l'app avec « Release apps to testing tracks » et « Manage testing tracks » (erreur « The Google service account cannot submit this app » sinon). Attendre quelques minutes.
4. Garder la clé JSON hors du projet (gestionnaire de mots de passe) : elle permet de publier sur le compte.
