import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_URL = "https://credit-risk-api.onrender.com"

st.set_page_config(page_title="📊 BI Dashboard", layout="wide")
st.title("📊 Tableau de bord - Data Analyst")

# Charger analytics
if st.button("Charger Statistiques Globales"):
    stats = requests.get(f"{API_URL}/analytics").json()
    st.json(stats)

# Explorer les demandes
limit = st.slider("Nombre de demandes à afficher", 10, 200, 50)
data = requests.get(f"{API_URL}/all_demandes/", params={"limit": limit}).json()
df = pd.DataFrame(data)

if not df.empty:
    st.dataframe(df, use_container_width=True)
    if "montant_prete" in df.columns:
        fig = px.histogram(df, x="montant_prete", nbins=20)
        st.plotly_chart(fig, use_container_width=True)
