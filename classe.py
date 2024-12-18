class Classe:
    def __init__(self, professeur: "Professeur"):
        self.professeur = professeur
        self.eleves = []

    def ajouter_eleve(self, eleve: "Eleve"):
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
        else:
            print("La classe est pleine !")

    def retirer_eleve(self, eleve: "Eleve"):
        if eleve in self.eleves:
            self.eleves.remove(eleve)

# Composants
class Professeur:
    def __init__(self, nom: str, matiere: str, dossier: "Dossier"):
        self.nom = nom
        self.matiere = matiere
        self.dossier = dossier

class Eleve:
    def __init__(self, nom: str, age: int, dossier: "Dossier"):
        self.nom = nom
        self.age = age
        self.dossier = dossier

class Dossier:
    def __init__(self, etat_civil: str, coordonnees: str):
        self.etat_civil = etat_civil
        self.coordonnees = coordonnees


if __name__ == "__main__":
    # Création d'un dossier pour le professeur
    dossier_prof = Dossier(etat_civil="M. Dupont", coordonnees="dupont@ecole.com")
    professeur = Professeur(nom="M. Dupont", matiere="Mathématiques", dossier=dossier_prof)

    # Création de la classe
    ma_classe = Classe(professeur=professeur)

    # Création d'élèves
    dossier_eleve1 = Dossier(etat_civil="Alice", coordonnees="alice@ecole.com")
    eleve1 = Eleve(nom="Alice", age=12, dossier=dossier_eleve1)

    dossier_eleve2 = Dossier(etat_civil="Bob", coordonnees="bob@ecole.com")
    eleve2 = Eleve(nom="Bob", age=13, dossier=dossier_eleve2)

    # Ajout des élèves
    ma_classe.ajouter_eleve(eleve1)
    ma_classe.ajouter_eleve(eleve2)

    # Affichage des informations
    print(f"Professeur : {ma_classe.professeur.nom}, Matière : {ma_classe.professeur.matiere}")
    print("Liste des élèves :")
    for eleve in ma_classe.eleves:
        print(f"- {eleve.nom}, Age : {eleve.age}, Dossier : {eleve.dossier.etat_civil}")

    # Retrait d'un élève
    ma_classe.retirer_eleve(eleve1)
    print("Après retrait d'un élève :")
    for eleve in ma_classe.eleves:
        print(f"- {eleve.nom}, Age : {eleve.age}")
