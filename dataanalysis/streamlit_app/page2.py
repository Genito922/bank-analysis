import streamlit as st
import pandas as pd
import requests
from sklearn.cluster import KMeans
import plotly.express as px

API_URL = "https://credit-risk-api.onrender.com"

st.set_page_config(page_title="🤖 ML Dashboard", layout="wide")
st.title("🤖 Modèles ML - Data Scientist")

# Charger données
limit = st.slider("Nombre de demandes à charger", 50, 500, 100)
data = requests.get(f"{API_URL}/all_demandes/", params={"limit": limit}).json()
df = pd.DataFrame(data)

if not df.empty:
    st.dataframe(df.head(20), use_container_width=True)

    if "montant_prete" in df.columns and "duree" in df.columns:
        # Petit clustering KMeans pour illustration
        X = df[["montant_prete", "duree"]].dropna()
        kmeans = KMeans(n_clusters=3, random_state=42).fit(X)
        df["cluster"] = kmeans.labels_

        fig = px.scatter(df, x="montant_prete", y="duree", color="cluster")
        st.plotly_chart(fig, use_container_width=True)
