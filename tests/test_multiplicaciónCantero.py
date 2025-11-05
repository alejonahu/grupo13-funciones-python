#tests/test_multiplicar.py
from funciones.multiplicacionCantero import multiplicar
def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10