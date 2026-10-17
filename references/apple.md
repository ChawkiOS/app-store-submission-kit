# App Store Connect, champ par champ

À jour d'octobre 2026. Si la console affiche autre chose, elle a raison.

## Informations sur l'app (une fois, valables pour toutes les versions)

| Champ | Limite | Conseils |
| --- | --- | --- |
| Nom | 30 caractères | Unique sur l'App Store. Nom seul, ou nom + accroche courte (« PATATE - Passe la bombe »). Pas de mots-clés empilés. |
| Sous-titre | 30 caractères | La promesse, avec le mot-clé principal. Indexé par la recherche. |
| Catégorie principale / secondaire | — | Jeux : jusqu'à 2 sous-catégories. Voir plus bas. |
| Droits relatifs au contenu | — | « Oui, contient du contenu tiers et je possède les droits » dès qu'il y a des sons, polices, images ou musiques de tiers sous licence (CC0, OFL, achat). « Non » seulement si tout est créé par l'éditeur. |
| Classification par âge | questionnaire | Voir plus bas. |
| URL de la politique de confidentialité | — | Obligatoire. Doit aussi être accessible **dans l'app** (règle 5.1.1). |
| Contrat de licence | — | Laisser le contrat standard d'Apple, sauf CGU spécifiques à lier. |

### Catégories

Apps : Achats, Actualités, Développeurs, Divertissement, Éducation, Finance, Forme et santé, Graphisme et design, Jeux, Livres, Médecine, Météo, Musique, Navigation, Photo et vidéo, Productivité, Référence, Réseaux sociaux, Restauration et boissons, Sports, Style de vie, Utilitaires, Voyages, Économie et entreprise, Enfants, Magazines et journaux.

Sous-catégories de **Jeux** (libellés de la console française) : Action, Aventure, Cartes, Casino, Casse-tête, Course, Famille, Jeux de rôle, Jeux de société, Mots, Musique, Parties rapides (= Casual), Quiz, Simulation, Sports, Stratégie.

Pièges : « Famille » fait penser à des enfants (et appelle les règles « Made for Kids ») ; « Jeux de société » désigne les jeux de plateau ; « Enfants » impose des règles strictes (pas de pub tierce, pas de lien externe sans contrôle parental).

## Page de la version (à chaque version)

| Champ | Limite | Conseils |
| --- | --- | --- |
| Texte promotionnel | 170 caractères | Modifiable sans nouvelle version : annonces, nouveautés, événements. Non indexé. |
| Description | 4 000 caractères | Pas d'emoji (refusés), pas de prix, pas de noms de concurrents. Première phrase = l'accroche. Non indexée par la recherche Apple. |
| Mots-clés | 100 caractères | Virgules **sans espace**. Ne pas répéter le nom, le sous-titre, la catégorie, ni « app » / « jeu » génériques sauf utiles. Pas de marques tierces. |
| Nouveautés de la version | 4 000 caractères | Pas pour la toute première version. |
| URL d'assistance | — | Obligatoire. La page doit donner un **moyen de contact** (e-mail ou formulaire). |
| URL marketing | — | Facultative. |
| Copyright | — | « 2026 Nom de l'éditeur ». |
| Captures et aperçus vidéo | — | Voir references/visuels.md. |
| Build | — | Envoyé par Xcode, Transporter ou `eas submit`. |
| Informations de connexion | — | Compte de démo si l'app demande une connexion. « Connexion requise : non » si compte anonyme automatique. |
| Notes de review | 4 000 caractères | En anglais. Voir plus bas. |
| Coordonnées pour la review | — | Prénom, nom, téléphone, e-mail joignables pendant la review. |
| Publication de la version | — | « Manuellement » pour choisir le jour de sortie (recommandé pour une première sortie coordonnée avec Google) ; « Automatiquement » ; ou publication progressive sur 7 jours. |

## Classification par âge (questionnaire, système 4+ / 9+ / 13+ / 16+ / 18+)

Pour chaque thème, répondre Aucun / Rare ou modéré / Fréquent ou intense, ou Oui / Non.

| Groupe | Questions | Comment répondre |
| --- | --- | --- |
| Fonctions de l'app | Accès Internet non restreint (navigateur intégré libre), contenu généré par les utilisateurs, messagerie et chat, publicité | Un pseudo visible par d'autres est un contenu généré par les utilisateurs (limité) ; un chat libre est « messagerie et chat ». Un lien vers un site précis n'est pas un accès Internet non restreint. |
| Thèmes matures | Grossièretés ou humour cru, horreur ou peur, alcool / tabac / drogue, thèmes matures ou suggestifs | « Rare ou modéré » dès qu'il y en a, même légers. |
| Médical ou bien-être | Informations médicales, traitements | Seulement si l'app en parle. |
| Sexualité ou nudité | — | — |
| Violence | Dessin animé ou fantastique, réaliste, prolongée ou graphique, armes à feu | Une explosion de dessin animé est « violence de dessin animé ou fantastique, rare ou modérée ». |
| Jeux de hasard | Jeux d'argent simulés, concours, coffres à butin | Un tirage au sort sans mise ni gain n'est pas un jeu d'argent. |
| Contrôles | Contrôle parental, vérification de l'âge | Seulement si l'app les a. |

« Made for Kids » : ne pas cocher sauf app conçue pour les moins de 13 ans (règles très strictes).

## Confidentialité de l'app (« étiquettes de confidentialité »)

1. « Collectez-vous des données ? » : oui dès qu'une donnée quitte le téléphone et est gardée (même un identifiant anonyme). Les données traitées uniquement sur l'appareil ne comptent pas.
2. Pour chaque type de donnée collecté : finalités, lié à l'identité de l'utilisateur ou non, utilisé pour le suivi (tracking) ou non.

Types de données : Coordonnées (nom, e-mail, téléphone, adresse, autres) · Santé et forme · Données financières · Localisation (précise, approximative) · Données sensibles · Contacts · Contenu de l'utilisateur (e-mails ou messages, photos ou vidéos, audio, contenu de jeu, service client, autre contenu) · Historique de navigation · Historique de recherche · Identifiants (identifiant de l'utilisateur, identifiant de l'appareil) · Achats · Données d'utilisation (interactions avec le produit, données publicitaires, autres) · Diagnostic (plantages, performances, autres) · Environnement · Corps · Autres données.

Finalités : Publicité tierce · Publicité ou marketing du développeur · Analyse · Personnalisation du produit · Fonctionnalité de l'app · Autres.

Repères :
- Identifiant de compte (même anonyme, Firebase par exemple) : Identifiants > Identifiant de l'utilisateur, lié, fonctionnalité.
- Pseudo : Contenu de l'utilisateur > Autre contenu (ou Coordonnées > Nom si c'est un vrai nom).
- Parties, scores, actions de jeu : Contenu de l'utilisateur > Contenu de jeu.
- Jeton de notification push : en général non déclaré (ce n'est pas un identifiant d'appareil au sens d'Apple) ; le déclarer en Identifiants > Identifiant de l'appareil seulement s'il sert à autre chose qu'envoyer des notifications.
- SDK d'analyse ou de crash (Crashlytics, Sentry, Analytics) : les déclarer (Diagnostic, Données d'utilisation).
- **Suivi (tracking)** : seulement si les données sont croisées avec celles d'autres entreprises pour de la publicité ciblée ou partagées avec des courtiers ; dans ce cas, App Tracking Transparency est obligatoire.

## Autres déclarations

| Question | Réponse habituelle |
| --- | --- |
| Conformité du chiffrement (export) | Avec `ITSAppUsesNonExemptEncryption = false` dans Info.plist (Expo : `ios.infoPlist`), la question ne se pose plus. Correct si l'app n'utilise que HTTPS et le chiffrement du système. |
| Identifiant publicitaire (IDFA) | Non, sauf SDK publicitaire ou d'attribution. |
| Contenu tiers | Voir « Droits relatifs au contenu ». |
| Tarifs et disponibilité | Gratuit, pays choisis ; pour une sortie en français seulement, tous les pays restent possibles. |

## Règles qui font refuser le plus souvent

- **2.1** : l'examinateur ne peut pas tester (connexion impossible, app vide sans autres joueurs) → compte de démo, mode solo, vidéo.
- **5.1.1(v)** : création de compte sans **suppression du compte dans l'app** → indiquer où elle se trouve dans les notes.
- **4.8** : connexion Google ou Facebook sans **Se connecter avec Apple**.
- **1.2** : contenu généré par les utilisateurs sans filtre, signalement et blocage.
- **2.3** : description, captures ou mots-clés qui promettent des fonctions absentes, ou mots-clés de marques tierces.
- **5.1.2** : données collectées non déclarées, ou politique de confidentialité absente de l'app.
- **3.1.1** : achats numériques hors du système d'Apple.

## Notes pour l'examinateur (modèle, en anglais)

> [App] is [ce que fait l'app en une phrase].
>
> [Connexion : « No login is required: the app creates an anonymous account on first launch. » ou identifiants du compte de démo.]
>
> To test on a single device: [étapes numérotées : mode solo, groupe de démo avec code, données préremplies].
>
> [Si multijoueur : code d'un groupe de démo avec des bots, et/ou lien vers une vidéo d'une partie complète.]
>
> Account deletion: [chemin exact dans l'app].
> [Blocage / signalement : chemin exact, si contenu entre utilisateurs.]

## TestFlight

- **Test interne** : jusqu'à 100 membres de l'équipe App Store Connect, **sans review**, disponible quelques minutes après le traitement du build.
- **Test externe** : jusqu'à 10 000 testeurs par e-mail ou lien public, après la **Beta App Review** (en général moins de 24 h). À remplir : description de la bêta, e-mail pour les retours, URL marketing, URL de confidentialité, « Quoi tester », informations de connexion.
- Un build TestFlight expire après 90 jours.

## Envoi d'un build (Expo / EAS)

```bash
npx eas-cli@latest build --platform ios --profile production
npx eas-cli@latest submit --platform ios --latest
```

EAS gère certificats, profils et capacités (Push, Associated Domains) si l'utilisateur se connecte à son compte Apple.
