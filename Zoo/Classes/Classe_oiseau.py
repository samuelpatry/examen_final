from Classes.Classe_Animal import Animal

class Oiseau(Animal):
    def __init__(self, p_longeur_bec : str = ""):
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille) #erreur dans l'héritage
        self._longeur_bec = p_longeur_bec

    @property
    def longeur_bec(self):
        return self._longeur_bec

    @longeur_bec.setter
    def longeur_bec(self, v_longeur_bec):
        if v_longeur_bec.isnumeric() and v_longeur_bec > 0:
            self._longeur_bec = v_longeur_bec
        else:
            raise ValueError("la longeur du bec est invalide")

