import streamlit as st

st.set_page_config(page_title="🏦 Bank Credit Risk", layout="wide")

st.title("🏦 Dashboard Crédit Risk")
page_0 = st.Page("page0.py", title="Bienvenue sur la plateforme d'analyse **Credit Risk**.", icon="🏠") # House
page_1 = st.Page("page1.py", title="Aperçu", icon="🏦")     # Bank clapperboard
page_2 = st.Page("page2.py", title= "**Data Analyst** : BI, exploration et reporting.", icon="👨‍💼")
page_3 = st.Page("page3.py", title="**Analytics avancées** : Statistiques globales et monitoring", icon = "📊")
page_4 =  st.Page( "page4.py", title="**Data Scientist** : ML, modèles de scoring et prédiction.", icon="🤖" )


pg = st.navigation([page_0, page_1, page_2, page_3, page_4])
pg.run()
