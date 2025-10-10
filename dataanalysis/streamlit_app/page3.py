import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# ========================
# Configuration
# ========================
API_BASE = "https://<ton-projet>.onrender.com"  # ⚠️ Remplace par ton URL Render

st.title("📊 Analytics Avancées - Crédit Risk")

# ========================
# Fonction utilitaire
# ========================
@st.cache_data
def fetch_data(endpoint: str):
    """Récupère les données JSON depuis l’API et les convertit en DataFrame"""
    url = f"{API_BASE}{endpoint}"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Erreur lors de l'appel à {url} : {e}")
        return pd.DataFrame()

# ========================
# Chargement des datasets
# ========================
demande_df = fetch_data("/demands")
agence_df = fetch_data("/agences")
client_df = fetch_data("/clients")
analytics_df = fetch_data("/analytics")   # Endpoint déjà prévu pour statistiques

# ========================
# Graphique 1 : Demandes de crédit par agence
# ========================
if not demande_df.empty and not agence_df.empty:
    demande_agence = demande_df.groupby("numero_agence").size().reset_index(name="count")
    fig_agence = px.bar(
        demande_agence,
        x="numero_agence",
        y="count",
        title="📌 Nombre de demandes de crédit par agence",
        labels={"numero_agence": "Agence", "count": "Nombre de demandes"},
        color="count",
        color_continuous_scale="viridis"
    )
    st.plotly_chart(fig_agence, use_container_width=True)

# ========================
# Graphique 2 : Montants prêtés par année
# ========================
if not demande_df.empty and "annee" in demande_df.columns:
    montant_par_annee = demande_df.groupby("annee")["montant_prete"].sum().reset_index()
    fig_montants = px.line(
        montant_par_annee,
        x="annee",
        y="montant_prete",
        title="💰 Montants prêtés par année",
        markers=True
    )
    st.plotly_chart(fig_montants, use_container_width=True)

# ========================
# Graphique 3 : Statistiques de l’endpoint /analytics
# ========================
if not analytics_df.empty:
    st.subheader("📈 Indicateurs clés (API /analytics)")
    st.dataframe(analytics_df)

    if "kpi" in analytics_df.columns and "valeur" in analytics_df.columns:
        fig_kpi = px.bar(
            analytics_df,
            x="kpi",
            y="valeur",
            title="Indicateurs globaux",
            color="valeur",
            color_continuous_scale="viridis"
        )
        st.plotly_chart(fig_kpi, use_container_width=True)

# ========================
# Graphique 4 : Répartition accord / refus
# ========================
if not demande_df.empty and "accord" in demande_df.columns:
    accord_stats = demande_df["accord"].value_counts().reset_index()
    accord_stats.columns = ["Accord", "Nombre"]
    fig_accord = px.pie(
        accord_stats,
        names="Accord",
        values="Nombre",
        title="✅ Répartition des accords vs refus"
    )
    st.plotly_chart(fig_accord, use_container_width=True)

# ========================
# Graphique 5 : Revenus clients vs montant demandé
# ========================
if not demande_df.empty and "revenu_mensuel_moyen" in demande_df.columns:
    fig_scatter = px.scatter(
        demande_df,
        x="revenu_mensuel_moyen",
        y="montant_prete",
        color="accord",
        size="apport",
        hover_data=["numero_demande", "numero_client"],
        title="📊 Revenus clients vs Montants demandés"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

st.success("✅ Analytics avancées chargées avec succès")
