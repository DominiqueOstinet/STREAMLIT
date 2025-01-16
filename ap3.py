import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur',
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur',
        },
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie
    "cookie key",          # La clé du cookie
    30,                    # Durée du cookie (en jours)
)

# Afficher le formulaire de connexion
authenticator.login()

# Vérifier l'état d'authentification
if st.session_state["authentication_status"]:
    # Créer la sidebar avec le menu
    with st.sidebar:
        # Message de bienvenue avec le nom de l'utilisateur
        st.write(f"Bienvenue, {st.session_state['username']}!")
        
        # Créer le menu avec les options Accueil et Photos
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Photos"]
        )

        # Bouton de déconnexion
        authenticator.logout("Déconnexion", "sidebar")

    # Afficher le contenu en fonction du choix de l'utilisateur
    if selection == "Accueil":
        st.title("Bienvenue sur ma page !")
        st.image("images/hello.png", use_container_width=True)
                 
    elif selection == "Photos":
        st.title("Bienvenue sur l'album photo de mon chat")

 # Afficher des photos 
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("images/cat1.png", use_container_width=True) 
        with col2:
            st.image("images/cat2.png", use_container_width=True) 
        with col3:
            st.image("images/cat3.png", use_container_width=True)

elif st.session_state["authentication_status"] is False:
    st.error("Le username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
