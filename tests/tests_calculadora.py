# tests/test_calculadora.py

import pytest
from calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(5, 3) == 2

def test_multiplicar():
    assert multiplicar(2, 3) == 6

def test_dividir():
    assert dividir(6, 3) == 2

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)
