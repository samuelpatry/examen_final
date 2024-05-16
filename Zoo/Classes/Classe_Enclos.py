


class Enclos:
    ls_animeaux = []
    ls_enclos = []
    nb_enclos = 0

    def __init__(self, p_numeros_enclos:str = "", p_nom_enclos: str = "", p_taille_enclos:str = "",
                 p_type_enclos:str = "", p_localistaion_enlos:str = ""):
        """
        Constructeur de la classe Enclos
        
        :param p_numeros_enclos: numeros de l'enclos
        :param p_nom_enclos: nom de l'enclos
        :param p_taille_enclos: taille de l'enclos
        :param p_type_enclos: type de l'enclos
        :param p_localistaion_enlos: localisation de l'enclos
        """
        self._numeros_enclos = p_numeros_enclos
        self._nom_enclos = p_nom_enclos
        self._taille_enclos = p_taille_enclos
        self._type_enclos = p_type_enclos
        self._localistaion_enlos = p_localistaion_enlos
        Enclos.ls_enclos.append(self)
        Enclos.nb_enclos += 1

    @property
    def numeros_enclos(self):
        return self._numeros_enclos
    @numeros_enclos.setter
    def numeros_enclos(self, v_numeros_enclos):
        if (isinstance(v_numeros_enclos, str) and len(v_numeros_enclos) == 8 and v_numeros_enclos[0:5].isalpha() and
                v_numeros_enclos[6:].isnumeric()):
            self._numeros_enclos = v_numeros_enclos
        else:
            raise ValueError("Le numeros de l'enclos est invalide")

    @property
    def nom_enclo(self):
        return self._nom_enclos
    @nom_enclo.setter
    def nom_enclo(self, v_nom_enclo):
        if isinstance(v_nom_enclo, str) and len(v_nom_enclo) <= 25:
            self._nom_enclo = v_nom_enclo
        else:
            raise ValueError("le type d'enclos est invalide")

    @property
    def taille_enclo(self):
        return self._taille_enclos

    @taille_enclo.setter
    def taille_enclo(self, v_taille_enclo):
        if v_taille_enclo == "petit" or "moyen" or "grand":
            self._taille_enclo = v_taille_enclo
        else:
            raise ValueError("la taille de l'enclos doit être petit ou moyen ou grand")

    @property
    def type_enclo(self):
        return self._type_enclos
    @type_enclo.setter
    def type_enclo(self, v_type_enclo):
        if v_type_enclo == "intérieur" or "extérieur":
            self._type_enclo = v_type_enclo
        else:
            raise ValueError("le type d'enclos est invalide (intérieur ou extérieur)")

    @property
    def localistaion_enlos(self):
        return self._localistaion_enlos

    @localistaion_enlos.setter
    def localistaion_enlos(self, v_localistaion_enlos):
        if v_localistaion_enlos == "A" or "B" or "C":
            self._localistaion_enlos = v_localistaion_enlos
        else:
            raise ValueError("le localisation de l'enclos est invalide (A, B, C)")

    def est_adapte(self,nbr_animaux):
        if nbr_animaux <= 2:
            self.taille_enclo == "petit"
            return True
        elif nbr_animaux <= 4:
            self.taille_enclo == "moyen"
            return True
        elif nbr_animaux <= 6:
            self.taille_enclo == "grand"
            return True
        else:
            return False