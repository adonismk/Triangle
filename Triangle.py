from math import*
from sys import*
# MWALE KALAISHA Adonis 
# Master 1
# Réseaux et Mobilité
#Travail Pratique d'Algorithmique Avancée sur les triangles


def Menu():
    
    print("**************************************************")
    print("                                                  ")
    print("*** 1. *** Saisir les informations du triangle ***")
    print("*** 2. *** Afficher les informations du triangle *")
    print("*** 3. ************ Type du triangle *************")
    print("*** 4. ************** La superficie **************")
    print("*** 5. ******** Trier selon la superficie ********")
    print("*** 6. ************** QUITER *********************")
    print("                                                  ")
    print("**************************************************")
    print("**************************************************")
    print("                                                  ")
    choix=int(input("Choisissez une option SVP!!!  "))


    return choix

if __name__ == "__main__":
    k=Menu()
    print("Donner les informations d'un triangle")

d=1
while d==1:
    a=(input("Saisir la première valeur  : ")) #l'utilisateur saisi la première valeur d'un coté du triangle

 
    if a=="":
        d=2

    elif a==a:
        b=(input("Saisir la deuxième valeur  : "))#l'utilisateur saisi la deuxième valeur d'un coté du triangle
        c=(input("Saisir la troisième valeur : "))#l'utilisateur saisi la troisième valeur d'un coté du triangle
        a,b,c=float(a),float(b),float(c)
        
    
        #formule pour un triangle rectangle
        if (a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b): 
            print("**************************************************")        
            print("C'est un triangle rectangle")
            print("**************************************************")

        #pour le cas où ce n'est pas un triangle
        elif ((a+b<=c) or ((a+c<=b) or (b+c<=a))):
            print("**************************************************")                 
            print("Ce N'est PAS un triangle")
            print("**************************************************")

        #Cas pour un triangle rectangle équilatéral
        elif (a==b or b==c or a==c):                               
            if a==b==c:
                print("**************************************************")
                print("C'est un triangle équilatéral") 
                print("**************************************************")

            #Cas pour un triangle rectangle isocèle
            elif (a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
                print("**************************************************")
                print("c'est un triangle rectangle isocèle")
                print("**************************************************")
                #Cas pour un triangle isocèle
            else:
                print("**************************************************")
                print("C'est un triangle isocèle")
                print("**************************************************")
        
        #Cas pour un triangle rectangle Scalène
        else:
            print("**************************************************")
            print("C'est un triangle Scalène")
            

exit()