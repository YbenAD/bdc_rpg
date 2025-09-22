#exemple d utilisation de la classe Personnage
from Personnage import Personnage
from Armes import Armes

epee_legendaire = Armes("Epee legendaire", 10)
jouer1 = Personnage("John", "Guerrier", 10, 1, 100, 10, 5, epee_legendaire)
jouer2 = Personnage("Jane", "Mage", 5, 1, 100, 5, 10)

jouer1.afficher_infos()
print()
jouer2.afficher_infos() 
print()
jouer1.attaquer(jouer2)
print()
jouer2.afficher_infos()