#importe toutes les bibliotheques dont on a besoin
import streamlit as st
import random 
import time
import numpy as np

# Classe Tamagotchi
# Permet de definir la santé initiale du tamagochi vu qu'il vient de "naitre" il est au maximum de sa forme donc à 100 dans toutes les catégories
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.faim = 100
        self.happiness = 100
        self.hygiene = 100
        self.sleep = 100
        
#vous présente le tamagotchi avec son nom à remplir, une image de lui et les barres de progression de sa santé en général
def accueil_page(my_tamagotchi):
    # Création d'une instance de Tamagotchi
    st.title("Tamagotchi - Accueil")
    tamagotchi_name = st.text_input("Entrer le nom du Tamagotchi:")
    my_tamagotchi = Tamagotchi(tamagotchi_name)
    st.header(f"Bonjour, {tamagotchi_name}!")
    
    st.image("base.png", width=200)
    
    st.subheader("Statut du Tamagotchi:")
    #à activer si la Sidebar ne fonctionne pas
    #st.write("Faim:", my_tamagotchi.faim)
    #st.write("Humeur:", my_tamagotchi.happiness)
    #st.write("Hygiene:", my_tamagotchi.hygiene)
    #st.write("Fatigue:", my_tamagotchi.sleep)
    sidebar()

    st.subheader("Tamagotchi Image:")
    #display_tamagotchi_hunger(my_tamagotchi)
    #display_tamagotchi_happiness(my_tamagotchi)
    #display_tamagotchi_hygiene(my_tamagotchi)
    #display_tamagotchi_sleep(my_tamagotchi)
    
    #st.image("base.png", width=200)

#La Sidebar permet de gérer la sante du Tamagochi, elles partent toutes à 100 et elles diminuent automatiquement toutes les 5 secondes, pour assurer la 
#bonne utilisations des barres sur toutes les pages, nous utilisons les cookies 
#si nous cliquons sur un bouton pour faire augmenter une fonction, les autres diminuent 
def sidebar():
    if 'Faim' not in st.session_state:
        st.session_state['Faim'] = 100
    barre_prog_f = st.progress(st.session_state['Faim'])
        
    #st.write("Faim :", st.session_state['Faim']) 
    barre_prog_f.progress(st.session_state['Faim'], f"Faim : {st.session_state['Faim']} %"  )
    
    if st.session_state['Faim'] >= 8 :
        st.session_state['Faim'] -= random.randint(1,7)
    else:
        st.session_state['Faim'] -= 1  
    
    if 'Hygiene' not in st.session_state:
    
        st.session_state['Hygiene'] = 100
        
    barre_prog_h = st.progress(st.session_state['Hygiene'], "Hygiene")
    
    
        
    barre_prog_h.progress(st.session_state['Hygiene'], f"Hygiene : {st.session_state['Hygiene']} %")
    
    
        
    #st.write("Hygiene :", st.session_state['Hygiene'])
    
    if st.session_state['Hygiene'] >= 8 :
        st.session_state['Hygiene'] -= random.randint(1,7)
    else:
        st.session_state['Hygiene'] -= 1
    
    
    
    if 'Humeur' not in st.session_state:
    
        st.session_state['Humeur'] = 100
        
    barre_prog_p = st.progress(st.session_state['Humeur'], "Humeur")
    
    
        
    barre_prog_p.progress(st.session_state['Humeur'], f"Humeur : {st.session_state['Humeur']} %")
    
    
            
      
    #st.write("Humeur :", st.session_state['Humeur'])
    
    if st.session_state['Humeur'] >= 8 :
        st.session_state['Humeur'] -= random.randint(1,7)
    else:
        st.session_state['Humeur'] -= 1
    
    if 'sommeil' not in st.session_state:
    
        st.session_state['sommeil'] = 100
        
    barre_prog_d = st.progress(st.session_state['sommeil'], "sommeil")
    
    barre_prog_d.progress(st.session_state['sommeil'], f"Fatigue : {st.session_state['sommeil']} %")
    
    
        
    #st.write("Dodo :", st.session_state['sommeil'])
    if st.session_state['sommeil'] >= 8 :
        st.session_state['sommeil'] -= random.randint(1,7)
    else:
        st.session_state['sommeil'] -= 1
    
    if st.session_state['sommeil'] <= 0:
        st.sidebar.write('Il est mort')
        st.stop()
        
    if st.session_state['Humeur'] <= 0:
        st.sidebar.write('Il est mort')
        st.stop() 
    if st.session_state['Hygiene'] <= 0:
        st.sidebar.write('Il est mort')
        st.stop()
        
    if st.session_state['Faim'] <= 0:
        st.sidebar.write('Il est mort')
        st.stop()   
        
    col1,col2,col3,col4,col5,col6,col7 = st.columns(7)

    with col1:
        if st.button('Manger'):
            if st.session_state['Faim'] >= 81 :
                st.session_state['Faim'] = 100
            if st.session_state['Faim'] <= 80 :
                st.session_state['Faim'] += 20
                    
            #Nous voulions faire en sorte que ce bouton emmène sur la page cuisine, mais nous n'avons pas trouvé comment faire...
              
    with col2:
        if st.button('Laver'):
            if st.session_state['Hygiene'] >= 81 :
                st.session_state['Hygiene'] = 100
            if st.session_state['Hygiene'] <= 80 :
                st.session_state['Hygiene'] += 20
            #Nous voulions faire en sorte que ce bouton emmène sur la page salle de bain, mais nous n'avons pas trouvé comment faire...
            
    with col3:   
        if st.button('Jouer' ):
            if st.session_state['Humeur'] >= 81 :
                st.session_state['Humeur'] = 100
            if st.session_state['Humeur'] <= 80 :
                st.session_state['Humeur'] += 20
            #Nous voulions faire en sorte que ce bouton emmène sur la page jeux, mais nous n'avons pas trouvé comment faire...
            
    with col4:    
        if st.button('Dormir'):
            if st.session_state['sommeil'] >= 81 :
                st.session_state['sommeil'] = 100
            if st.session_state['sommeil'] <= 80 :
                st.session_state['sommeil'] += 20
            #Nous voulions faire en sorte que ce bouton emmène sur la page chambre, mais nous n'avons pas trouvé comment faire...
            
    #st.balloons()
    #l'animation st.balloons nous a permis de verifier le bon fonctionnement de la commande toutes les 5 secondes 
    time.sleep(5)
    
    st.rerun()
    pass

def regles_page():
    st.title("Tamagochi - Comment Jouer ?")
    st.header("Bienvenue à vous, avant de commencer à vous amuser, expliquons les règles !")
    st.write(" ")
    st.write("Le tamagotchi doit toujours avoir ses barres de capacité le plus haut possible, si une des barres atteint 0%, c'est fini. ")
    st.write("Pour augmenter le niveau des barres, il faut changer de pièce :")
    st.write("-pour l'hygiène, il faut aller dans la salle de bain ")
    st.write("-pour la faim, il faut aller dans la cuisine")
    st.write("-pour la fatigue, il faut aller dans la chambre.")
    st.write("Pour la joie c'est un peu différent :")
    st.write("-il faut jouer à un des trois mini-jeux disponible dans la page jeux : le pile ou face, le pair ou impair ou pierre-feuille-ciseaux.")
    st.write(" ")
    st.write(" Amusez-vous bien ! ")
    st.write("Pour une expérience optimale, changez les couleurs de la page en suivant l'image suivante :")
    st.image('config-couleurs.png', caption='Couleurs à paramétrer', use_column_width=False, width=300)
    
    sidebar()
    
    #st.write("depechez vous de jouer ou les barres tomberont à 0")
    
#définition de la cuisine avec ses images et ses boutons
def cuisine_page():
    st.title("Tamagotchi - Cuisine")
    
    tab1, tab2 = st.columns(2)
    
    with tab1:
        col1,col2 = st.columns(2)
        with col1:
            placeholder = st.empty()
            import random

            placeholder.image("hungry.png",width= 200)
        with col2:
            viande = st.button("Viande")
            legumes = st.button("Légumes")
            fruit = st.button("Fruit")
            fromage = st.button("Fromage")
        if viande == True:
            if st.session_state['Faim'] >= 81 :
                st.session_state['Faim'] = 100
            if st.session_state['Faim'] <= 80 :
                st.session_state['Faim'] += 20
            with col1:
                placeholder.image("healthy.png",width= 200)
        if legumes == True:
            if st.session_state['Faim'] >= 81 :
                st.session_state['Faim'] = 100
            if st.session_state['Faim'] <= 80 :
                st.session_state['Faim'] += 20
            with col1:
                placeholder.image("healthy.png",width= 200)  
        if fruit == True:
            if st.session_state['Faim'] >= 81 :
                st.session_state['Faim'] = 100
            if st.session_state['Faim'] <= 80 :
                st.session_state['Faim'] += 20
            with col1:
                placeholder.image("healthy.png",width= 200)
        if fromage == True:
            if st.session_state['Faim'] >= 81 :
                st.session_state['Faim'] = 100
            if st.session_state['Faim'] <= 80 :
                st.session_state['Faim'] += 20
            with col1:
                placeholder.image("healthy.png",width= 200)
    
    with tab2:
        col1,col2 = st.columns(2)
        with col1:
            placeholder = st.empty()
            placeholder.image("thirsty.png",width= 200)
        with col2:
            eau = st.button("Eau")
            lait = st.button("Lait")
            jusdefruits = st.button("Jus de fruits")
        if eau == True:
            if st.session_state['Faim'] >= 81 :
                st.session_state['Faim'] = 100
            if st.session_state['Faim'] <= 80 :
                st.session_state['Faim'] += 20
            with col1:
                placeholder.image("satiate.png",width= 200)
        if lait == True:
            if st.session_state['Faim'] >= 81 :
                st.session_state['Faim'] = 100
            if st.session_state['Faim'] <= 80 :
                st.session_state['Faim'] += 20
            with col1:
                placeholder.image("satiate.png",width= 200)  
        if jusdefruits == True:
            if st.session_state['Faim'] >= 81 :
                st.session_state['Faim'] = 100
            if st.session_state['Faim'] <= 80 :
                st.session_state['Faim'] += 20
            with col1:
                placeholder.image("satiate.png",width= 200)  

    sidebar()
#définition de la salle de bain avec ses images et ses boutons
def salle_de_bains_page():
    st.title("Tamagotchi - Salle de bains")
    col1,col2 = st.columns(2)
    with col1:
        placeholder = st.empty()
        placeholder.image("dirty.png", width= 200)
    with col2:
        savon = st.button("Savon")
        douche = st.button("Douche")
    if savon == True:
        if st.session_state['Hygiene'] >= 81 :
            st.session_state['Hygiene'] = 100
        if st.session_state['Hygiene'] <= 80 :
            st.session_state['Hygiene'] += 20
        with col1:
            placeholder.image("bathroom.png",width= 200)
    if douche == True:
        if st.session_state['Hygiene'] >= 81 :
            st.session_state['Hygiene'] = 100
        if st.session_state['Hygiene'] <= 80 :
            st.session_state['Hygiene'] += 20
        with col1:
            placeholder.image("wet.png",width= 200)
            
    sidebar()
#définition de la chambre avec ses images et ses boutons
def chambre_page():
    st.title("Tamagotchi - Chambre")
    col1,col2 = st.columns(2)
    with col1:
        placeholder = st.empty()
        placeholder.image("tired.png", width= 200)
    with col2:
        dormir = st.button("Au dodo")
    if dormir == True:
        if st.session_state['sommeil'] >= 81 :
            st.session_state['sommeil'] = 100
        if st.session_state['sommeil'] <= 80 :
            st.session_state['sommeil'] += 20
        with col1:
            placeholder.image("happy.png",width= 200)
            
    sidebar()
#définition de la page jeux avec ses images, ses boutons et ses jeux
def jeux_page():

    st.title("Tamagotchi - Jeux")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.image("maths.png", width= 200)
        st.write("Pair ou impair ?")
    with col2:
        st.image("coin.png", width= 200)
        st.write("Pile ou Face")
    with col3:
        st.image("controler.png", width= 200)
        st.write("Pierre-Feuille-Ciseaux")
    #if calc == True: 


    #à l'origine, un jeu de calcul mental était prévu, cependant nous n'avons pas réussi à résoudre les problèmes qu'il engendrait
    #nous l'avons remplacé par ce jeu dont la mécanique est proche du pile ou face
    st.title("Pair ou impair ?")
    # Initialisation des compteurs
    victoire1 = st.session_state.get("victoires", 0)
    defaite1 = st.session_state.get("defaites", 0)

    # Création des boutons
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
    with col1:
        bouton_pair = st.button("Pair")
    with col2:
        bouton_impair = st.button("Impair")

    # Génération d'un nombre aléatoire entre 0 et 1
    resultat1 = np.random.rand()

    # Conversion en Pair ou impair
    if resultat1 > 0.5:
        resultat1 = "Impair"
    else:
        resultat1 = "Pair"

    # Mise à jour des compteurs
    if bouton_pair:
        if resultat1 == "Pair":
            victoire1 += 1
            st.balloons()
            st.write("Vous avez choisi Pair et vous avez gagné!")
            if st.session_state['Humeur'] >= 81 :
                st.session_state['Humeur'] = 100
            if st.session_state['Humeur'] <= 80 :
                st.session_state['Humeur'] += 20
            #gain de points d'humeur car heureux de gagner
        else:
            defaite1 += 1
            st.write("Vous avez choisi Pair et vous avez perdu!")
            if st.session_state['Humeur'] <= 20 :
                st.session_state['Humeur'] = 0
            if st.session_state['Humeur'] >= 21 :
                st.session_state['Humeur'] += 20
            #perte de points d''humeur car le hasard n'est pas avec vous 

    if bouton_impair:
        if resultat1 == "Impair":
            victoire1 += 1
            st.balloons()
            st.write("Vous avez choisi Impair et vous avez gagné!")
            if st.session_state['Humeur'] >= 81 :
                st.session_state['Humeur'] = 100
            if st.session_state['Humeur'] <= 80 :
                st.session_state['Humeur'] += 20
            #gain de points d'humeur car heureux de gagner
        else:
            defaite1 += 1
            st.write("Vous avez choisi Impair et vous avez perdu!")
            if st.session_state['Humeur'] <= 20 :
                st.session_state['Humeur'] = 0
            if st.session_state['Humeur'] >= 21 :
                st.session_state['Humeur'] += 20
            #perte de points d''humeur car le hasard n'est pas avec vous

    # Sauvegarde des valeurs des compteurs
    st.session_state["victoires"] = victoire1
    st.session_state["defaites"] = defaite1

    # Affichage des résultats
    st.write("Victoires: ", victoire1)
    st.write("Défaites: ", defaite1)

            # Fonction pour générer un choix aléatoire pour l'ordinateur
    def get_computer_choice():
        choices = ['pierre', 'feuille', 'ciseaux']
        return random.choice(choices)

    # Fonction pour déterminer le gagnant
    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'égalité'
        elif (user_choice == 'pierre' and computer_choice == 'ciseaux') or \
             (user_choice == 'feuille' and computer_choice == 'pierre') or \
             (user_choice == 'ciseaux' and computer_choice == 'feuille'):
            return 'utilisateur'
        else:
            return 'ordinateur'



    
    # Création de la page Streamlit
    st.title('Pierre-Feuille-Ciseaux')

    if 'user_score' not in st.session_state:
        
        st.session_state['user_score'] = 0
        
    if 'computer_score' not in st.session_state:
        
        st.session_state['computer_score'] = 0

    # Création des boutons de choix
    user_choice = st.radio('Choisissez votre coup :', ('pierre', 'feuille', 'ciseaux'))

    # Génération du choix de l'ordinateur
    if st.button('valider'):
        computer_choice = get_computer_choice()

        # Affichage des choix
        st.write('Utilisateur a choisi :', user_choice)
        st.write('Ordinateur a choisi :', computer_choice)

        # Détermination du gagnant
        winner = determine_winner(user_choice, computer_choice)

        # Mise à jour des scores
        if winner == 'utilisateur':
            st.balloons()
            st.session_state['user_score'] += 1
            st.write('Bravo, vous avez gagné !')
            if st.session_state['Humeur'] >= 81 :
                st.session_state['Humeur'] = 100
            if st.session_state['Humeur'] <= 80 :
                st.session_state['Humeur'] += 20
            #gain de points d'humeur car heureux de gagner
        elif winner == 'ordinateur':
            st.session_state['computer_score'] += 1
            st.write('Dommage, vous avez perdu...')
            if st.session_state['Humeur'] <= 20 :
                st.session_state['Humeur'] = 0
            if st.session_state['Humeur'] >= 21 :
                st.session_state['Humeur'] += 20
            #perte de points d''humeur car le hasard n'est pas avec vous 
        else:
            st.write('C\'est un match nul !')
            if st.session_state['Humeur'] >= 91 :
                st.session_state['Humeur'] = 100
            if st.session_state['Humeur'] <= 90 :
                st.session_state['Humeur'] += 10
            #gain de points d'humeur car heureux de jouer

    # Affichage des scores
    st.write('Score utilisateur :', st.session_state['user_score'])
    st.write('Score ordinateur :', st.session_state['computer_score'])

    def get_computer_choice():
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)


    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return 'user'
        else:
            return 'computer'

    st.title("Pile ou Face")
    # Initialisation des compteurs
    victoire = st.session_state.get("victoire", 0)
    defaite = st.session_state.get("defaite", 0)

    # Création des boutons
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
    with col1:
        bouton_pile = st.button("Pile")
    with col2:
        bouton_face = st.button("Face")

    # Génération d'un nombre aléatoire entre 0 et 1
    resultat = np.random.rand()

    # Conversion en pile ou face
    if resultat > 0.5:
        resultat = "Pile"
    else:
        resultat = "Face"

    # Mise à jour des compteurs
    if bouton_pile:
        if resultat == "Pile":
            victoire += 1
            st.balloons()
            st.write("Vous avez choisi Pile et vous avez gagné!")
            if st.session_state['Humeur'] >= 81 :
                st.session_state['Humeur'] = 100
            if st.session_state['Humeur'] <= 80 :
                st.session_state['Humeur'] += 20
            #gain de points d'humeur car heureux de gagner
        else:
            defaite += 1
            st.write("Vous avez choisi Pile et vous avez perdu!")
            if st.session_state['Humeur'] <= 20 :
                st.session_state['Humeur'] = 0
            if st.session_state['Humeur'] >= 21 :
                st.session_state['Humeur'] += 20
            #perte de points d''humeur car le hasard n'est pas avec vous 

    if bouton_face:
        if resultat == "Face":
            victoire += 1
            st.balloons()
            st.write("Vous avez choisi Face et vous avez gagné!")
            if st.session_state['Humeur'] >= 81 :
                st.session_state['Humeur'] = 100
            if st.session_state['Humeur'] <= 80 :
                st.session_state['Humeur'] += 20
            #gain de points d'humeur car heureux de gagner
        else:
            defaite += 1
            st.write("Vous avez choisi Face et vous avez perdu!")
            if st.session_state['Humeur'] <= 20 :
                st.session_state['Humeur'] = 0
            if st.session_state['Humeur'] >= 21 :
                st.session_state['Humeur'] += 20
            #perte de points d''humeur car le hasard n'est pas avec vous

    # Sauvegarde des valeurs des compteurs
    st.session_state["victoire"] = victoire
    st.session_state["defaite"] = defaite

    # Affichage des résultats
    st.write("Victoires: ", victoire)
    st.write("Défaites: ", defaite)
        
    sidebar()


def display_tamagotchi_hunger(tamagotchi):
    if tamagotchi.faim >= 80:
        st.image("base.png", width=200)
    elif 60 <= tamagotchi.faim < 80:
        st.image("starving.png", width=200)
    else:
        st.image("hungry.png", width=200)

def display_tamagotchi_happiness(tamagotchi):
    if tamagotchi.happiness >= 80:
        st.image("happy.png", width=200)
    elif 60 <= tamagotchi.happiness < 80:
        st.image("base.png", width=200)
    else:
        st.image("triste.png", width=200)

def display_tamagotchi_hygiene(tamagotchi):
    if tamagotchi.hygiene >= 80:
        st.image("clean.png", width=200)
    elif 60 <= tamagotchi.hygiene < 80:
        st.image("filthy.png", width=200)
    else:
        st.image("dirty.png", width=200)

def display_tamagotchi_sleep(tamagotchi):
    if tamagotchi.sleep >= 80:
        st.image("awake.png", width=200)
    elif 60 <= tamagotchi.sleep < 80:
        st.image("tired.png", width=200)
    else:
        st.image("sleeping.png", width=200)


def choix_pieces(page):

    if page == "Accueil":
        my_tamagotchi = Tamagotchi("Tamagotchi")
        accueil_page(my_tamagotchi)
    elif page == "Cuisine":
        cuisine_page()
    elif page == "Salle de bains":
        salle_de_bains_page()
    elif page == "Chambre":
        chambre_page()
    elif page == "Jeux":
        jeux_page()
    elif page == "Règles" :
        regles_page()

def main():
    page = st.sidebar.selectbox('Choisissez une page:', ["Accueil","Règles", "Cuisine", "Salle de bains", "Chambre", "Jeux"])
    choix_pieces(page)

if __name__ == "__main__":
    main()

#projet réalisé par Pierre Le Bris (Chef de projet), Lise Bernadi (direction artistique), Titouan Desbordes(Codeur), Cyril Pimont(Codeur)