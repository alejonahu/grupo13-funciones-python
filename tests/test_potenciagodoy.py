from funciones.potenciagodoy import potenciagodoy

def test_potenciagodoy():

    assert potenciagodoy(2, 3) == 8
    assert potenciagodoy(5, 0) == 1
