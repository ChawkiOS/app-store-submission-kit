#!/usr/bin/env python3
"""Vérifie un fichier STORE.md : limites de caractères et mots-clés Apple.

Usage : python3 verifier_store.py STORE.md

Chaque champ s'écrit ainsi dans STORE.md (titre en gras avec sa limite, puis le texte en citation) :

    **Sous-titre App Store** (30 caractères max) :

    > La patate chaude entre amis

La limite est lue dans la parenthèse (« 30 caractères max », « 4 000 caractères max », « 100 characters max »).
Pour un texte sur plusieurs lignes de citation, les lignes sont réunies avec des retours à la ligne,
et le gras Markdown (**…**) est retiré, comme dans la console.
Les mots-clés (champ dont le titre contient « mots-clés » ou « keywords ») sont aussi vérifiés :
virgules sans espace, pas de doublon, pas de mot du nom ou du sous-titre de la même section.
"""
import re
import sys
import unicodedata

TITRE = re.compile(r'^\*\*(.+?)\*\*\s*\(([^)]*?)(\d[\d\s.  ]*)\s*(?:caract|charac)[^)]*\)', re.I)


def nettoyer(texte: str) -> str:
    texte = re.sub(r'\*\*(.+?)\*\*', r'\1', texte)
    return unicodedata.normalize('NFC', texte)


def lire_champs(lignes):
    champs = []
    section = ''
    i = 0
    while i < len(lignes):
        ligne = lignes[i]
        if ligne.startswith('## '):
            section = ligne[3:].strip()
        m = TITRE.match(ligne.strip())
        if m:
            nom = m.group(1).strip()
            limite = int(re.sub(r'\D', '', m.group(3)))
            j = i + 1
            while j < len(lignes) and not lignes[j].startswith('>'):
                if lignes[j].startswith('**') or lignes[j].startswith('#'):
                    break
                j += 1
            bloc = []
            while j < len(lignes) and lignes[j].startswith('>'):
                bloc.append(lignes[j][1:].removeprefix(' '))
                j += 1
            texte = nettoyer('\n'.join(bloc).strip())
            # Valeur écrite sur la même ligne : « **Nom** (30 caractères max) : PATATE ».
            en_ligne = ligne.strip()[m.end():].split(':', 1)
            if not texte and len(en_ligne) == 2 and en_ligne[1].strip():
                texte = nettoyer(en_ligne[1].strip())
            champs.append({'section': section, 'nom': nom, 'limite': limite, 'texte': texte, 'ligne': i + 1})
            i = j
            continue
        i += 1
    return champs


def verifier_mots_cles(champ, champs):
    problemes = []
    texte = champ['texte']
    if ', ' in texte:
        problemes.append('espace après une virgule (Apple compte chaque espace)')
    mots = [m.strip() for m in texte.split(',') if m.strip()]
    vus = set()
    for mot in mots:
        cle = mot.lower()
        if cle in vus:
            problemes.append(f'doublon : « {mot} »')
        vus.add(cle)
    # Mots déjà indexés par Apple : nom et sous-titre de la même section.
    deja = set()
    for autre in champs:
        if autre['section'] == champ['section'] and re.search(r'\b(nom|name|sous-titre|subtitle)\b', autre['nom'], re.I):
            deja.update(w.lower() for w in re.findall(r'\w+', autre['texte']))
    for mot in mots:
        for w in re.findall(r'\w+', mot):
            if w.lower() in deja and len(w) > 2:
                problemes.append(f'« {w} » est déjà dans le nom ou le sous-titre (inutile dans les mots-clés)')
    return problemes


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    lignes = open(sys.argv[1], encoding='utf-8').read().split('\n')
    champs = lire_champs(lignes)
    if not champs:
        sys.exit('Aucun champ « **Titre** (N caractères max) » trouvé.')
    erreurs = 0
    for champ in champs:
        longueur = len(champ['texte'])
        etat = 'ok' if 0 < longueur <= champ['limite'] else ('VIDE' if longueur == 0 else 'TROP LONG')
        if etat != 'ok':
            erreurs += 1
        print(f"{etat:9} {longueur:5}/{champ['limite']:<5} {champ['section'][:18]:18} {champ['nom']} (ligne {champ['ligne']})")
        if re.search(r'mots-cl|keyword|palabras clave|palavras-chave|schlüsselw|parole chiave', champ['nom'], re.I):
            for p in verifier_mots_cles(champ, champs):
                erreurs += 1
                print(f'          mots-clés : {p}')
    print('\nTout est dans les limites.' if erreurs == 0 else f'\n{erreurs} problème(s) à corriger.')
    sys.exit(1 if erreurs else 0)


if __name__ == '__main__':
    main()
