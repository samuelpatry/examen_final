import pytest
from Classes.Classe_Enclos import Enclos

#test méthode est atapté

@pytest.mark.parametrize("valeur_envoyer, valeur_prevue", [
    (1, True),
    (2, True),
    (3, True),
    (4, True),
    (5, True),
    (6, True),
    (7, False),
    (8, False),
    (9, False),
    (10, False),
    (1280, False),
])
def test__enclos(valeur_envoyer, valeur_prevue):
    enclos = Enclos()
    assert enclos.est_adapte(valeur_envoyer) == valeur_prevue




