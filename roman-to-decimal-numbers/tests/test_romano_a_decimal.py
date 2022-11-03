import pytest

from romano_a_decimal import romano_a_decimal

EQUIVALENCIAS: dict[str, int] = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


@pytest.mark.parametrize("test_input,esperado", EQUIVALENCIAS.items())
def test_numeros_estandar(test_input, esperado):
    assert romano_a_decimal(test_input) == esperado


@pytest.mark.parametrize("test_input,esperado", [("IX", 9), ("IV", 4)])
def test_numeros_con_sustraccion(test_input, esperado):
    assert romano_a_decimal(test_input) == esperado


def test_numero_mas_grande():
    assert romano_a_decimal("MMMCMXCIX") == 3_999


@pytest.mark.parametrize("test_input,esperado", [("IX", 9), ("ix", 9)])
def test_acepta_caracteres_en_distintos_formatos(test_input, esperado):
    assert romano_a_decimal(test_input) == esperado


def test_levanta_excepcion_con_string_vacio():
    with pytest.raises(ValueError):
        romano_a_decimal("")


def test_levanta_excepcion_con_primer_caracter_invalid():
    """Este caso existe especificamente porque siempre tomamos el primer caracter y sacamos
    su equivalencia antes de empezar a iterar sobre el numeral romano"""
    with pytest.raises(KeyError):
        romano_a_decimal("P")


@pytest.mark.parametrize("test_input", ["P", "IP", "XXLOL"])
def test_levanta_excepcion_con_caracteres_invalidos(test_input):
    with pytest.raises(KeyError):
        romano_a_decimal(test_input)
