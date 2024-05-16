import pytest
from Classes.Classe_Veterinaire import Veterinaire

#test méthode prendre retraite

@pytest.mark.parametrize("valeur_envoyer, valeur_prevue", [
    (1, False),
    (2, False),
    (3, False),
    (4, False),
    (5, False),
    (6, False),
    (7, False),
    (8, False),
    (9, False),
    (10, False),
    (55, False),
    (60, True),
    (65, True),
    (75, True),
    (85, True),
    (95, True),
    (105, True),
])
def test__enclos(valeur_envoyer, valeur_prevue):
    veterinaire = Veterinaire()
    assert veterinaire.prendre_retraitre() == valeur_prevue