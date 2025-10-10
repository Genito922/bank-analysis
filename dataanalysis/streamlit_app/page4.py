# page2.py → Data Scientist ML
import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title("🤖 Data Scientist – Analyse & Prédictions ML")

# URL de ton API FastAPI (adapter si besoin)
API_URL = "https://api-risk-credit.onrender.com"

# =========================
# 1. Charger les données brutes depuis l’API
# =========================
st.subheader("📥 Données brutes")
try:
    response = requests.get(f"{API_URL}/all_demandes?limit=100")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.dataframe(df.head(10), use_container_width=True)
    else:
        st.error("Erreur lors du chargement des données depuis l’API")
        df = pd.DataFrame()
except Exception as e:
    st.error(f"Impossible de contacter l’API: {e}")
    df = pd.DataFrame()

# =========================
# 2. Features Engineering
# =========================
if not df.empty:
    st.subheader("⚙️ Feature Engineering")

    # Exemple : calcul du ratio apport/revenu et durée normalisée
    if {"apport", "revenu_mensuel_moyen", "duree"}.issubset(df.columns):
        df["ratio_apport_revenu"] = df["apport"] / (df["revenu_mensuel_moyen"] + 1)
        df["duree_norm"] = (df["duree"] - df["duree"].mean()) / df["duree"].std()

        st.write("Nouvelles features générées : `ratio_apport_revenu`, `duree_norm`")
        st.dataframe(df[["apport", "revenu_mensuel_moyen", "ratio_apport_revenu", "duree", "duree_norm"]].head(10))

        # Visualisation interactive
        fig = px.scatter(
            df,
            x="ratio_apport_revenu",
            y="duree_norm",
            color="accord",
            title="Feature Engineering – Ratio apport/revenu vs Durée normalisée"
        )
        st.plotly_chart(fig, use_container_width=True)

# =========================
# 3. Analytics depuis l’API
# =========================
st.subheader("📊 Analytics API")
try:
    response = requests.get(f"{API_URL}/analytics")
    if response.status_code == 200:
        analytics = response.json()
        st.json(analytics)
    else:
        st.warning("Impossible de récupérer les analytics depuis l’API")
except Exception as e:
    st.error(f"Erreur API: {e}")

# =========================
# 4. Prédictions ML
# =========================
st.subheader("🔮 Prédictions ML")

if not df.empty:
    # On simule ici un appel ML (adapter selon ton endpoint réel ex: /predict)
    if st.button("Lancer les prédictions"):
        try:
            # Exemple : on envoie seulement 5 lignes pour tester
            sample_data = df.head(5).to_dict(orient="records")
            response = requests.post(f"{API_URL}/predict", json=sample_data)

            if response.status_code == 200:
                preds = response.json()
                preds_df = pd.DataFrame(preds)
                st.success("Prédictions reçues ✅")
                st.dataframe(preds_df)
            else:
                st.error("Erreur dans la prédiction ML depuis l’API")
        except Exception as e:
            st.error(f"Erreur API prédiction: {e}")
