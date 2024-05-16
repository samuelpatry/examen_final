from Classes.Classe_Animal import Animal


class Mammifere(Animal):

    def __init__(self, p_couleur_poil: str = ""):
       """
       Constructeur de la classe mammifere
       :param p_couleur_poil:
       """

       Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille) #erreur dans l'héritage
       self.p_couleur_poil = p_couleur_poil

    @property
    def couleur_poil(self):
        return self.p_couleur_poil

    @couleur_poil.setter
    def couleur_poil(self, v_couleur_poil):
        if v_couleur_poil == "noire" or "blanche" or "brune" or "grise" or "beige" or " multi couleurs":
            self.p_couleur_poil = v_couleur_poil
        else:
            return ValueError("la couleur du poil de l'animal est invalide")






