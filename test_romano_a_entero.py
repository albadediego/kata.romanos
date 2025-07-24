from main import romano_a_entero, RomanNumberError
import pytest

def test_romano_a_entero_I():
    assert romano_a_entero('I') == 1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero('MDCCXIII') == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero('IV') == 4

def test_romano_a_entero_no_repetir_mas_de_tres_01():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("IIII")
    assert str(exceptionInfo.value) == "No se puede repetir el valor más de tres veces"

def test_romano_a_entero_no_repetir_mas_de_tres_02():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("XXXX")
    assert str(exceptionInfo.value) == "No se puede repetir el valor más de tres veces"

def test_romano_a_entero_no_repetir_mas_de_tres_03():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("CCCC")
    assert str(exceptionInfo.value) == "No se puede repetir el valor más de tres veces"

def test_romano_a_entero_no_repetir_mas_de_tres_04():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("MMMM")
    assert str(exceptionInfo.value) == "No se puede repetir el valor más de tres veces"

def test_romano_a_entero_no_repetir_mas_de_una_01():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("DD")
    assert str(exceptionInfo.value) == "Los caracteres 'D', 'L' y 'V' no se pueden repetir."

def test_romano_a_entero_no_repetir_mas_de_una_02():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("LL")
    assert str(exceptionInfo.value) == "Los caracteres 'D', 'L' y 'V' no se pueden repetir."

def test_romano_a_entero_no_repetir_mas_de_una_03():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("VV")
    assert str(exceptionInfo.value) == "Los caracteres 'D', 'L' y 'V' no se pueden repetir."

def test_romano_a_entero_restar_solo_I_VX():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("IL")
    assert str(exceptionInfo.value) == "I solo se puede restar de V y X"

def test_romano_a_entero_restar_solo_X_LC():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("XM")
    assert str(exceptionInfo.value) == "X solo se puede restar de L y C"

'''
def test_romano_a_entero_restar_solo_C_DM():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("XM")
    assert str(exceptionInfo.value) == "C solo se puede restar de D y M"
'''

def test_romano_a_entero_no_se_resta_V():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("VX")
    assert str(exceptionInfo.value) == "V, L y D nunca se pueden restar"

def test_romano_a_entero_no_se_resta_L():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("LC")
    assert str(exceptionInfo.value) == "V, L y D nunca se pueden restar"

def test_romano_a_entero_no_se_resta_D():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("DM")
    assert str(exceptionInfo.value) == "V, L y D nunca se pueden restar"
