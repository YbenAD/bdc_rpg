from tabulate import tabulate


class Personnage:
    def __init__(self, nom, classe, attaque, niveau, points_de_vie, force, intelligence):
        self.nom = nom
        self.classe = classe
        self.attaque = attaque
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence
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
            ["Etat", etat]
        ]
        print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
    
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} ")
        degats = self.force * 2
        cible.subir_degats(degats)
        
    def subir_degats(self, degats):
        self.points_de_vie -= degats        
        print(f"{self.nom} subit {degats} points de degats.")
          