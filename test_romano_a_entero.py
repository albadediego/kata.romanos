from main import romano_a_entero

def test_romano_a_entero_I():
    assert romano_a_entero('I') == 1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero('MDCCXIII') == 1713

#def test_romano_a_entero_IV():
#    assert romano_a_entero('IV') == 4