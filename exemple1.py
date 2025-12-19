#Carte avec les led

################# Init
presence = 0 # 0 = Pas là. 1 = Là
alumage_rouge = False
alumage_vert = True
#################

while True:
    ... #Prend le message de exemple2.pe
    if presence == 0:
        alumage_rouge = False
        alumage_vert = True
    else:
        alumage_rouge = True
        alumage_vert = False