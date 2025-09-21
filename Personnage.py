class Personnage:
    def __init__(self, nom, classe, attaque, niveau, points_de_vie, force, intelligence):
        self.nom = nom
        self.classe = classe
        self.attaque = attaque
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence
        
    def afficher_infos(self):
        print("Nom:", self.nom)
        print("Classe:", self.classe)
        print("Attaque:", self.attaque)
        print("Niveau:", self.niveau)
        print("Points de vie:", self.points_de_vie)
        print("Force:", self.force)
        print("Intelligence:", self.intelligence)
        
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} ")
        degats = self.force * 2
        cible.subir_degats(degats)
        
    def subir_degats(self, degats):
        self.points_de_vie -= degats        
        print(f"{self.nom} subit {degats} points de degats.")
          