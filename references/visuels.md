# Visuels des stores

À jour d'octobre 2026. Vérifier dans la console : quand une taille est refusée, le message d'erreur donne les tailles acceptées.

## Apple

| Visuel | Taille | Remarques |
| --- | --- | --- |
| Icône | 1024 × 1024, sans transparence ni coins arrondis | Fournie par le build (Expo : `icon` dans `app.json`). |
| Captures iPhone 6,9 pouces (obligatoires) | 1320 × 2868 (ou 1290 × 2796) | Jusqu'à 10. Apple les réutilise pour les écrans plus petits : déposer dans l'onglet **6,9 pouces**. |
| Captures iPhone 6,1 / 6,3 pouces (si demandées) | 1206 × 2622 (ou 1179 × 2556) | Seulement si la console insiste. |
| Captures iPad 13 pouces | 2064 × 2752 | Obligatoires seulement si l'app tourne sur iPad (`supportsTablet`). |
| Aperçu vidéo | 886 × 1920 ou 1920 × 886, 15 à 30 s | Facultatif. Uniquement des images de l'app. |
| En-tête / mise en avant | 5244 × 2950 et 3840 × 1646 | Demandés pour les événements et la mise en avant. Sujet centré, rien d'important près des bords. |
| Résultats de recherche | 5244 × 2950 | Même règle. |

## Google Play

| Visuel | Taille | Remarques |
| --- | --- | --- |
| Icône | 512 × 512, PNG ou JPEG, 1 Mo max | Google applique la forme et l'ombre. |
| Bannière (feature graphic) | 1024 × 500, 15 Mo max | Obligatoire. |
| Captures téléphone | 2 à 8, côtés entre 320 et 3840 px, rapport 2:1 max | 1080 × 1920 (9:16) conseillé ; au moins 4 en 1080 px pour être mis en avant. |
| Captures tablette 7 et 10 pouces | — | Seulement si l'app vise les tablettes. |

## Captures : quoi montrer

- 4 à 6 captures, dans l'ordre du parcours qui donne envie : le moment le plus fort d'abord (pas l'écran de connexion).
- Une légende courte en haut de chaque capture (4 à 6 mots), un mot mis en valeur, une phrase d'explication au plus.
- De **vrais écrans** de l'app, dans un cadre de téléphone ; les mêmes visuels servent aux deux stores, aux bonnes tailles.
- Pas de faux contenus trompeurs, pas de prix, pas de badges « n°1 », pas de logos d'Apple ou Google, pas de pseudos réels de proches (utiliser des comptes de démo).
- Une série par langue de fiche : les légendes et l'app affichées dans la langue de la fiche.

## Produire les visuels

Avec le script du skill (voir SKILL.md, étape 4) : `visuels.json` décrit la marque et les captures de chaque langue, `scripts/rendre_visuels.py` rend tout aux bonnes tailles avec Chrome sans interface, et une planche par langue permet de tout vérifier d'un coup.

Bon à savoir :
- Prendre les écrans bruts sur un vrai téléphone (iPhone 6,9 pouces : 1320 × 2868 natif) pendant une partie de démo, **après** la fin des animations.
- Chrome sans interface impose une fenêtre d'au moins 500 px de large : pour voir une page à largeur de téléphone, la mettre dans une `iframe` de 375 px.
- Vérifier les tailles avec `sips -g pixelWidth -g pixelHeight` (le script le fait pour chaque fichier).
- Rangement : `store/<langue>/ios/`, `store/<langue>/android/`, `store/android/icone-512.png`, `store/captures-brutes/<langue>/`, `visuels.json` à la racine.
