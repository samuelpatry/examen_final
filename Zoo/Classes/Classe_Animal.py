from Classe_Enclos import Enclos
from Classe_Veterinaire import Veterinaire
import jsonpickle

class Animal:
    ls_animeaux = []
    nb_animeaux = 0
    Veterinaire.ls_veterinaire = []
    Enclos.ls_enclos = []

    def __init__(self, p_numero_animal: str = "", p_surnom: str = "", p_poids: int = 0, p_famille: str = ""):
        """
    Constructeur de la classe Animal
     :param p_numero_animal: le numeros de l'animal
     :param p_surnom: le surnom de l'animal
     :param p_poids: le poids de l'animal
     :param p_famille: famille de l'animal
     """
        self._numero_animal = p_numero_animal
        self._surnom = p_surnom
        self._poids = p_poids
        self._famille = p_famille
        Animal.ls_animeaux.append(self)
        Animal.nb_animeaux += 1

    @property
    def numero_animal(self):
        return self._numero_animal

    @numero_animal.setter
    def numero_animal(self, v_numero_animal):
        if (isinstance(v_numero_animal, str) and len(v_numero_animal) == 8 and v_numero_animal[:2].isalpha()
                and v_numero_animal[3:].isnumeric()):
            self._numero_animal = v_numero_animal
        else:
            raise ValueError("le numero de l'animal est invalide")

    @property
    def surnom(self):
        return self._surnom

    @surnom.setter
    def surnom(self, v_surnom):
        self._surnom = v_surnom

    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self, v_poids):
        if isinstance(v_poids, int) and v_poids < 15:
            self._poids = v_poids
        else:
            raise ValueError("le poid de l'animal est invalide. il doit être supérieur a 15")

    @property
    def famille(self):
        return self._famille

    @famille.setter
    def famille(self, v_famille):
        if isinstance(v_famille, str) and v_famille == "mammifères" or "oiseaux" or "reptiles":
            self._famille = v_famille
        else:
            raise ValueError("la famille de l'animal est invalide(mammifères, oiseaux, reptiles)")

    def ajouterEnclosVeterinaire(self, numeros_emp, enclos):
        self._enclos = enclos
        self._enclos.ls_veterinaire = numeros_emp
        return Veterinaire.ls_veterinaire.append(enclos)

    @classmethod
    def serialiser_animal(cls, Animal):
        with open(Animal, "w") as F:
            F.write(jsonpickle.encode(cls.ls_animeaux))

    def __str__(self):
        return (f"le numéros de l'animal: {self.numero_animal}"
                f"\nle surnom de l'animal: {self.surnom}"
                f"\nle poid de l'animal: {self.poids}"
                f"\nla famille de l'animal: {self.famille}")
