from Classes.Classe_Animal import Animal

class Reptile(Animal):
    def __init__(self, p_venimeux : bool = False):
        Animal.__init__(self, p_numero_animal, p_surnom, p_poids, p_famille) #erreur dans l'héritage
        self._venimeux = p_venimeux

    @property
    def venimeux(self):
        return self._venimeux

    @venimeux.setter
    def venimeux(self, v_venimeux):
        self._venimeux = v_venimeux