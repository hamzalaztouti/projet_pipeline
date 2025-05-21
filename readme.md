# 🚋 PIPELINE SNCF – PostgreSQL & Python

## 🖍️ PRÉSENTATION DU PROJET

Ce projet met en place un pipeline ELT (Extract - Load - Transform) de traitement de données ferroviaires issues d'un fichier CSV de la SNCF. L'objectif est d'importer ces données dans une base PostgreSQL, de les structurer et de les rendre exploitables pour des analyses de ponctualité, retards et annulations.

### Étapes réalisées :

* Affichage et prévisualisation des données brutes
* Nettoyage et renommage des colonnes
* Chargement dans la base PostgreSQL (table raw_sncf2)
* Transformation et création de la table nettoyée clean_sncf
* Suppression des colonnes inutiles ou nulles
* Visualisation avec Streamlit et analyse des KPIs

## 🔺 ORGANISATION DU RÉPERTOIRE

project_pipeline/
├── data/
│   └── sncf.csv
├── SQL/
│   ├── transform_clean_sncf.sql
├── scripts/
│   └── load_to_postgres.py
├── app.py
└── README.md


## 🔢 INSTRUCTIONS D'EXÉCUTION

### Prérequis

* Python 3.8+
* PostgreSQL installé localement (user: postgres, mdp: admin123)

### Installation des dépendances

pip install pandas sqlalchemy psycopg2 streamlit


### Lancement du pipeline

python scripts/load_to_postgres.py


### Lancement de l'application de visualisation

streamlit run app.py


## 🏛️ SCHÉMA RELATIONNEL

Deux tables principales :

* raw_sncf2 : données brutes importées
* clean_sncf : données nettoyées et préparées pour l'analyse

Champs conservés : date, service, gares de départ/arrivée, durée, retards, annulations, etc.

## 📈 ANALYSES POSSIBLES

* Top 5 des gares avec le retard moyen le plus élevé
* Évolution du retard moyen par mois
* Proportion de trains annulés par station de départ
* Distribution des retards > 15min/30min/60min

## 👩‍💻 AUTEUR

Hamza Laztouti

lizoul Meryem

Aourachi Yassine

* Projet réalisé dans le cadre du module Data Engineering (HETIC 2025)