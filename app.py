import streamlit as st
import pandas as pd
import sqlalchemy

# Connexion à PostgreSQL
engine = sqlalchemy.create_engine("postgresql://postgres:admin123@localhost:5432/sncf")

# Chargement des données transformées
@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM clean_sncf", engine)

df = load_data()

# -----------------------------
# 🌐 Interface Streamlit
# -----------------------------

st.set_page_config(page_title="Analyse SNCF", layout="wide")

st.title("🚆 Analyse des Retards et Annulations - SNCF")
st.markdown("""
Cette application permet d'explorer les retards, annulations et performances des trains SNCF, à partir de données ouvertes.

  
**Projet ELT - HETIC 2025**
""")

# 📝 Filtres interactiv
st.sidebar.header("🔍 Filtres")
selected_gare = st.sidebar.selectbox("Choisir une gare de départ", df["gare_depart"].dropna().unique())
df_filtered = df[df["gare_depart"] == selected_gare]

# 📊 KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Durée moyenne du trajet (min)", round(df_filtered["duree_trajet"].mean(), 2))
col2.metric("Retard moyen (min)", round(df_filtered["retard_moyen_depart"].mean(), 2))
col3.metric("% d'annulations", f"{round(100 * df_filtered['trains_annules'].sum() / df_filtered['circulations_prevues'].sum(), 2)} %")

st.markdown("---")

# 🌐 Affichage des données filtrées
st.subheader(f"Données pour la gare : {selected_gare}")
st.dataframe(df_filtered, height=300)

# 🌎 Visualisations
import altair as alt

st.subheader("🎨 Top 5 des gares avec le plus de retards au départ")
top_retards = df.groupby("gare_depart")["trains_retard_depart"].sum().sort_values(ascending=False).head(5).reset_index()
chart_retards = alt.Chart(top_retards).mark_bar().encode(
    x=alt.X("trains_retard_depart", title="Nombre total de retards"),
    y=alt.Y("gare_depart", sort="-x", title="Gare de départ")
)
st.altair_chart(chart_retards, use_container_width=True)

st.subheader("🕰️ Top 5 gares avec la plus longue durée moyenne")
top_durees = df.groupby("gare_depart")["duree_trajet"].mean().sort_values(ascending=False).head(5).reset_index()
chart_durees = alt.Chart(top_durees).mark_bar(color="#4e79a7").encode(
    x=alt.X("duree_trajet", title="Durée moyenne (min)"),
    y=alt.Y("gare_depart", sort="-x", title="Gare de départ")
)
st.altair_chart(chart_durees, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Projet réalisé par **Hamza Laztouti**, **Meryem Lizoul**, **Yassine Aourachi**")