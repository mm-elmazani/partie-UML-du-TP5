class Animal:
    def __init__(self, nom: str, habitat: "Habitat"):
        self.nom = nom
        self.habitat = habitat
        self.tete = Tete()
        self.corps = Corps()
        self.membres = Membres()

class Herbivore(Animal):
    def __init__(self, nom: str, habitat: "Habitat"):
        super().__init__(nom, habitat)

class Carnivore(Animal):
    def __init__(self, nom: str, habitat: "Habitat"):
        super().__init__(nom, habitat)

# Composants
class Habitat:
    def __init__(self, type_habitat: str):
        self.type = type_habitat

class Tete:
    pass

class Corps:
    pass

class Membres:
    pass



if __name__ == "__main__":
    # Création d'un habitat
    habitat_foret = Habitat(type_habitat="Forêt")

    # Création d'un animal Herbivore
    lapin = Herbivore(nom="Lapin Blanc", habitat=habitat_foret)

    # Création d'un animal Carnivore
    lion = Carnivore(nom="Lion Fier", habitat=habitat_foret)

    # Tests d'affichage
    print(f"Nom de l'herbivore : {lapin.nom}, Habitat : {lapin.habitat.type}")
    print(f"Nom du carnivore : {lion.nom}, Habitat : {lion.habitat.type}")

    # Vérification des composants
    print("Le lapin possède :")
    print(f"- Une tête : {lapin.tete}")
    print(f"- Un corps : {lapin.corps}")
    print(f"- Des membres : {lapin.membres}")
