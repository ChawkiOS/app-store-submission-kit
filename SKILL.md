---
name: fiches-stores
description: Prépare TOUT ce qu'il faut pour publier une app sur l'App Store (App Store Connect) et Google Play (Play Console) à partir d'une spécification et des maquettes — textes des fiches dans les langues choisies (nom, sous-titre, descriptions, mots-clés, texte promotionnel, notes de version), catégories et tags, URLs, réponses à tous les questionnaires (classification d'âge Apple et IARC, confidentialité Apple, sécurité des données Google, contenu de l'app, droits, chiffrement), notes de review, tests interne et fermé, et les visuels rendus aux tailles exactes dans chaque langue (captures iPhone et Android, en-têtes et visuel de recherche Apple, bannière et icône Google), le tout dans un STORE.md vérifié et un dossier store/. Use when the user asks to prepare, write or fill an App Store / Google Play listing, store screenshots, feature graphic, store description, keywords, metadata, age rating, privacy or data safety answers, review notes, TestFlight or closed testing, or "la fiche store", "les fiches des stores", "les visuels des stores", "préparer la soumission".
---

# Fiches et visuels App Store et Google Play

Produit, à partir de la spécification et des maquettes de l'app :

1. **`STORE.md`** à la racine du projet : chaque champ des deux consoles, dans chaque langue choisie, avec sa réponse prête et sa raison.
2. **`store/`** : tous les visuels aux tailles exactes, dans chaque langue, prêts à déposer, avec une planche de contrôle par langue.

L'utilisateur ne devrait plus avoir à réfléchir devant un formulaire ni ouvrir un outil de design.

Références (lire celle de l'étape en cours) :

- [references/langues.md](references/langues.md) : codes de langue des deux stores, adaptation, variantes régionales.
- [references/apple.md](references/apple.md) : App Store Connect, champ par champ.
- [references/google.md](references/google.md) : Play Console, champ par champ, questionnaire IARC pas à pas.
- [references/visuels.md](references/visuels.md) : tailles exactes et règles des visuels.
- [modele/STORE.md](modele/STORE.md) et [modele/visuels.json](modele/visuels.json) : squelettes à remplir.
- `scripts/verifier_store.py` : limites de caractères et mots-clés.
- `scripts/rendre_visuels.py` (avec `modeles-visuels/`) : rendu de tous les visuels, toutes langues.

Les règles des stores changent. Références à jour d'octobre 2026 ; si la console affiche autre chose, elle a raison : adapter et le signaler.

## 1. Demander les langues et les maquettes (toujours, en premier)

Avant d'écrire quoi que ce soit, s'assurer d'avoir ces deux réponses. Si l'utilisateur les a déjà données dans sa demande (« prépare la fiche en anglais, espagnol et français »), ne pas les redemander.

1. **Dans quelles langues préparer les fiches ?** Proposer les langues que l'app contient déjà (fichiers de traduction), et rappeler qu'une fiche dans une langue absente de l'app trompe le joueur (voir references/langues.md). Préciser la variante quand elle compte (espagnol d'Amérique latine ou d'Espagne, portugais du Brésil ou du Portugal) et la **langue principale** de la fiche.
2. **Où sont les maquettes ou les écrans ?** Accepter tout ce qui montre l'app :
   - des **captures réelles** de l'app (le mieux : Apple veut des captures qui montrent l'app telle qu'elle est) ;
   - des **images de maquettes** (PNG, JPG, PDF) ;
   - un **artefact ou une page HTML** de maquettes (le lire avec l'outil Artifact ou l'ouvrir, puis rendre chaque écran à 1320 × 2868 avec Chrome) ;
   - un lien **Figma** (utiliser le skill figma pour exporter les écrans) ;
   - à défaut, proposer de capturer l'app sur un téléphone (en mode démo, dans chaque langue).
   Demander aussi, si le projet ne les donne pas : couleurs et polices de la marque, mascotte ou logo pour les bannières.

Poser ces questions **en un seul message**, avec les autres faits manquants de l'étape 2 (5 questions au plus en tout, chacune avec une proposition par défaut).

## 2. Rassembler les faits

Lire, dans le projet : la spécification (SPECIFICATION.md, README, docs), la config de l'app (`app.json` / `app.config.*`, `Info.plist`, `AndroidManifest.xml`, `build.gradle`), les fichiers de traduction, le site (confidentialité, CGU), le thème (couleurs, polices), et le code là où il répond à une question.

| Fait | Où le trouver |
| --- | --- |
| Nom, bundle ID iOS, package Android, version | config de l'app |
| Ce que fait l'app, pour qui, ce qui la rend différente | spécification |
| Langues disponibles dans l'app | fichiers de traduction |
| Gratuit ou payant, achats intégrés, abonnements, publicité | spécification, dépendances (SDK pub, RevenueCat, StoreKit, Billing) |
| Compte : aucun, anonyme, e-mail, connexion Apple/Google | code d'authentification |
| Données collectées, pourquoi, prestataires (Firebase, Expo, analytics…) | code, politique de confidentialité |
| Contenu entre utilisateurs (texte libre, photos, chat), blocage, signalement | code, spécification |
| Âge minimum, public visé | CGU, spécification |
| Permissions natives réellement demandées | manifeste final, Info.plist |
| Contenus tiers (sons, polices, images) et licences | assets, spécification |
| URLs : site, assistance (avec un contact), confidentialité, suppression du compte | site |
| Contact, éditeur, copyright | site, utilisateur |
| Comment un examinateur teste l'app seul (démo, mode solo, vidéo) | spécification |
| Couleurs, polices, logo, mascotte | thème, assets |

**Ne rien inventer** : un fait introuvable devient une question (étape 1).

## 3. Écrire STORE.md

Partir de [modele/STORE.md](modele/STORE.md). Sections, dans l'ordre où on remplit les consoles :

1. **Règles d'écriture** propres à l'app.
2. **Textes, une section par langue** (langue principale d'abord) : nom App Store, nom Google Play, sous-titre, description courte, texte promotionnel, description complète, mots-clés, notes de version. Chaque langue est **écrite pour elle** (references/langues.md), avec ses propres mots-clés.
3. **Catégories et tags**.
4. **URLs et contact**.
5. **Âge** : questionnaire Apple, IARC pas à pas, public cible.
6. **Confidentialité** : Apple, puis sécurité des données Google.
7. **Déclarations** : droits sur le contenu, chiffrement, publicité, accès à l'app, finances, santé, actualités, gouvernement, identifiant publicitaire.
8. **Review** : notes en anglais, coordonnées, accès Google.
9. **Tests** : TestFlight, test interne et fermé Google (12 testeurs pendant 14 jours pour un compte personnel récent), instructions aux testeurs dans leurs langues.
10. **Visuels** : liste des fichiers produits par langue (étape 4).
11. **Checklist** de soumission.

Règles des textes :
- Première phrase de la description = l'accroche (seule visible avant « plus »). Puis sections courtes à titre en majuscules, puces, appel à l'action.
- Concret (ce qu'on fait dans l'app) plutôt qu'adjectifs ; vrai (seulement la version soumise ; « bientôt » seulement dans le texte promotionnel Apple).
- Mots-clés Apple : 100 caractères, virgules sans espace, sans répéter nom, sous-titre ni catégorie, sans marques tierces.
- Pas d'emoji dans les textes Apple. Neutre en genre quand la langue le permet.

Règles des réponses :
- Chaque réponse donne sa **raison**. Honnête plutôt qu'avantageux (une réponse minimisée fait refuser ou retirer l'app plus tard).
- Cohérent avec la politique de confidentialité, le code et l'autre store ; signaler toute contradiction.
- Libellés tels qu'ils apparaissent dans la console (anglais pour la Play Console si elle est en anglais ; dans le doute, les deux).

## 4. Produire les visuels

1. **Écrans** : rassembler un écran par capture et par langue dans `store/captures-brutes/<langue>/` (1320 × 2868 de préférence ; une autre taille de téléphone convient, le cadre s'adapte avec `ratio_ecran`). Depuis une maquette HTML : rendre chaque écran avec Chrome sans interface à la taille du téléphone. Retoucher seulement ce qui ne trahit pas l'app (pseudos de test, données de démo).
2. **Choisir 4 à 6 captures** dans l'ordre du parcours qui donne envie (references/visuels.md), avec pour chacune : étiquette, titre (un mot mis en valeur avec `<em>`), phrase, couleur de fond, un autocollant. Les écrire **dans chaque langue**.
3. **Remplir `visuels.json`** à la racine du projet à partir de [modele/visuels.json](modele/visuels.json) : nom, icône, mascotte ou logo, couleurs et polices de la marque, et pour chaque langue la bannière (accroche, pastille, 2 bulles) et les captures.
4. **Rendre** :

   ```bash
   python3 ~/.claude/skills/fiches-stores/scripts/rendre_visuels.py visuels.json
   ```

   Produit pour chaque langue : captures Apple 6,9 et 6,3 pouces, captures Google, en-tête Apple 5244 × 2950 et 3840 × 1646, visuel de recherche Apple 5244 × 2950, bannière Google 1024 × 500 ; plus l'icône Google 512 et une `planche.png` par langue. `--langue en` ou `--seulement captures|bannieres|icone` pour refaire une partie.
5. **Regarder chaque planche** (Read sur l'image, réduite avec `sips -Z` si elle est grande) : texte qui déborde ou se coupe, mot seul en fin de titre, autocollant qui cache l'information importante, contraste. Corriger `visuels.json` et refaire la partie concernée jusqu'à ce que tout soit propre.
6. Si la marque ne colle pas aux modèles (style très différent), copier `modeles-visuels/` dans le projet et adapter le HTML ; le script accepte les mêmes paramètres.

## 5. Vérifier

```bash
python3 ~/.claude/skills/fiches-stores/scripts/verifier_store.py STORE.md
```

Corriger jusqu'à « Tout est dans les limites ». Puis relire comme un examinateur : chaque promesse existe-t-elle dans l'app ? Chaque réponse de confidentialité correspond-elle au code et à la politique ?

## 6. Livrer

- `STORE.md` (mettre à jour l'existant en gardant ce qui est déjà validé) et `store/` (avec `visuels.json` et les écrans bruts, pour pouvoir tout refaire).
- Dans le message : les langues couvertes, les fichiers produits, les **choix à valider** (catégorie, âge, nom affiché, captures), les réponses sensibles à relire (âge, confidentialité) et ce qui manque.
- Ensuite, accompagner l'utilisateur écran par écran dans les consoles : quand il colle une question de formulaire, répondre avec la valeur exacte à choisir et la raison en une ligne, dans la langue de la question.
