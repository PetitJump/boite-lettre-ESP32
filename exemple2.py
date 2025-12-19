#Carte avec le capteur IR

################# Init
presence = 0 # 0 = Pas là. 1 = Là
attente = 5 #Le nombre de seconde a attendre entre chaque update
#################

seconde = 0
attente += 1 #Pour que le programme attendre vraiment le nombre de seconde

while True:
    if attente == seconde:
        presence = ... #Regarde le capteur et regarde si il renvoie 0 ou 1
        ... #Envoie la valeur de 'presence' à exemple1.py
        seconde = 0

    seconde += 1
    ... #Attendre 1s