import streamlit as st
import os

FICHIER = "sql_km.txt"

st.title("Knowledge Management - SQL")

# Fonction pour ajouter un concept
def ajouter_concept(titre, description):
    with open(FICHIER, "a", encoding="utf-8") as f:
        f.write(f"{titre}|{description}\n")

# Fonction pour lister les concepts
def lister_concepts():
    if not os.path.exists(FICHIER):
        return []
    with open(FICHIER, "r", encoding="utf-8") as f:
        return [ligne.strip().split("|") for ligne in f.readlines()]

# Fonction pour supprimer un concept
def supprimer_concept(index):
    lignes = lister_concepts()
    if 0 <= index < len(lignes):
        lignes.pop(index)
        with open(FICHIER, "w", encoding="utf-8") as f:
            for t, d in lignes:
                f.write(f"{t}|{d}\n")

# Ajouter un concept
st.header("Ajouter un concept SQL")
titre = st.text_input("Titre")
description = st.text_area("Description")
if st.button("Ajouter"):
    if titre and description:
        ajouter_concept(titre, description)
        st.success("Concept ajouté !")

# Rechercher un concept
st.header("Rechercher un concept")
mot_cle = st.text_input("Mot-clé pour recherche")
if st.button("Rechercher"):
    concepts = lister_concepts()
    trouve = False
    for t, d in concepts:
        if mot_cle.lower() in t.lower() or mot_cle.lower() in d.lower():
            st.write(f"**{t}** : {d}")
            trouve = True
    if not trouve:
        st.info("Aucun concept trouvé.")

# Lister et supprimer les concepts
st.header("Liste de tous les concepts SQL")
concepts = lister_concepts()
for i, (t, d) in enumerate(concepts):
    col1, col2 = st.columns([6,1])
    col1.write(f"**{t}** : {d}")
    if col2.button("Supprimer", key=i):
        supprimer_concept(i)
        st.experimental_rerun()