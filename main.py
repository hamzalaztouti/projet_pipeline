import pandas as pd
from sqlalchemy import create_engine

# Lire le CSV avec bon encodage et bon séparateur
df = pd.read_csv("sncf.csv", encoding="ISO-8859-1", sep=";", on_bad_lines='skip')

# Nettoyer les noms de colonnes
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_").str.replace("'", "")
df.columns = df.columns.str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")

# Connexion PostgreSQL
engine = create_engine('postgresql://postgres:admin123@localhost:5432/sncf')

# Charger dans PostgreSQL avec une table propre
df.to_sql("raw_sncf2", engine, if_exists="replace", index=False)

print(" Données bien structurées chargées dans PostgreSQL.")
