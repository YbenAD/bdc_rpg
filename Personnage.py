from tabulate import tabulate
from Armes import Armes


class Personnage:
    def __init__(self, nom, classe, attaque, niveau, points_de_vie, force, intelligence, Armes=None):
        self.nom = nom
        self.classe = classe
        self.attaque = attaque
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence
        self.Armes = Armes
        self.en_vie = True
        
    def afficher_infos(self):
        etat = "Vivant" if self.en_vie else "Mort"
        
        table = [
            ["Nom", self.nom],
            ["Classe", self.classe],
            ["Niveau", self.niveau],
            ["Points de vie", self.points_de_vie],
            ["Force", self.force],
            ["Intelligence", self.intelligence],
            ["Arme", self.Armes.nom if self.Armes else "aucune arme eqipuee" ],
            ["degats de l arme", self.Armes.degats if self.Armes else 0],
            ["Etat", etat]
        ]
        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
    
    def attaquer(self, cible):
        if self.Armes:
            print(f"{self.nom} attaque {cible.nom} avec {self.Armes.nom}.")
            degats = self.force * 2 + self.Armes.degats
        else:
            print(f"{self.nom} attaque {cible.nom}.")
            degats = self.force * 2
            
        cible.subir_degats(degats)
        
    def subir_degats(self, degats):
        self.points_de_vie -= degats        
        print(f"{self.nom} subit {degats} points de degats.")
          