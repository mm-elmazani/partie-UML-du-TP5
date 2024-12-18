
class Email:
    def __init__(self, expediteur: str, destinataire: str, titre: str = "", texte: str = ""):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.fichiers_joints = []

    def ajouter_fichier(self, fichier: "FichierJoint"):
        self.fichiers_joints.append(fichier)

    def supprimer_fichier(self, fichier: "FichierJoint"):
        if fichier in self.fichiers_joints:
            self.fichiers_joints.remove(fichier)

# Composant
class FichierJoint:
    def __init__(self, nom: str, taille: int):
        self.nom = nom
        self.taille = taille



if __name__ == "__main__":
    # Création d'un email
    email = Email(expediteur="alice@example.com", destinataire="bob@example.com", titre="Projet", texte="Voici le projet.")

    # Ajout de fichiers joints
    fichier1 = FichierJoint(nom="rapport.pdf", taille=1024)
    fichier2 = FichierJoint(nom="image.png", taille=512)

    email.ajouter_fichier(fichier1)
    email.ajouter_fichier(fichier2)

    # Tests d'affichage
    print(f"Email de {email.expediteur} à {email.destinataire}")
    print("Fichiers joints :")
    for fichier in email.fichiers_joints:
        print(f"- {fichier.nom} ({fichier.taille} Ko)")

    # Suppression d'un fichier
    email.supprimer_fichier(fichier1)
    print("Après suppression d'un fichier :")
    for fichier in email.fichiers_joints:
        print(f"- {fichier.nom} ({fichier.taille} Ko)")
