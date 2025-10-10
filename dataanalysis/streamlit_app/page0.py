import streamlit as st

# Interface utilisateur avec Streamlit
st.set_page_config(
    layout="wide",
    page_title="BANK Data Analysis",
    page_icon="🏦"  # Emoji Unicode directement
)

# Conteneur pour aligner les éléments horizontalement
col1, col2, col3 = st.columns([1, 4, 1])

# Colonne gauche : Image
with col1:
    st.image(
        "https://media.licdn.com/dms/image/v2/D4D03AQHzUzJ0V1_fzg/profile-displayphoto-shrink_800_800/B4DZTVqfHRHkAg-/0/1738751472693?e=1762387200&v=beta&t=xlL5cs7pVU8cN4m6ZTpP7GzKi8RBD2Mu2A2noHmM7uc",  # Remplacez par le chemin de votre image
        width=80,     # Ajustez la taille si nécessaire
        use_container_width=False,
    )

# Colonne centrale : Titre
with col2:
    st.markdown(
        """
        <h1 style='text-align: center; margin-bottom: 0;'>Exploration des Données Bancaire</h1>
        """,
        unsafe_allow_html=True,
    )

# Colonne droite : Nom et lien LinkedIn
with col3:
    st.markdown(
        """
        <div style='text-align: right;'>
            <a href="https://www.linkedin.com/in/moh-adjonlin-jean-claude-n-douba-7737bb342/" target="_blank" style='text-decoration: none; color: #0077b5;'>
                <strong>N'DOUBA MÔH</strong>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write(" ")
st.write(" ")

# Titre
st.markdown("# **Phase 1 : Développeur Python & Architecte API**")
# Afficher l'image séparément
st.image("https://raw.githubusercontent.com/JosueAfouda/films-analytics/main/streamlit_app/architecture.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/Genito922/api_risk_credit" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📦 Cliquer pour voir le Code de la Phase 1
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.write(" ")
st.write(" ")
st.write(" ")


# Titre
st.markdown("# **Phase 2 : Data Analyst - Exploration Visualisation et Data Scientist - Machine Learning**")
# Afficher l'image séparément
st.image("https://raw.githubusercontent.com/JosueAfouda/films-analytics/main/streamlit_app/architecturephase.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/Genito922/bank-analysis" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📊 Cliquer pour voir le Code de la Phase 2
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )