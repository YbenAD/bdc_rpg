#exemple d utilisation de la classe Personnage
from Personnage import Personnage

jouer1 = Personnage("John", "Guerrier", 10, 1, 100, 10, 5)
jouer2 = Personnage("Jane", "Mage", 5, 1, 100, 5, 10)

jouer1.afficher_infos()
print()
jouer2.afficher_infos() 
print()
jouer1.attaquer(jouer2)
print()
jouer2.afficher_infos()