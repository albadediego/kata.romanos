from main import entero_a_romano

valor_romano = entero_a_romano(1994)

def test_prueba_entero_a_romano():
    assert valor_romano == 'MCMXCIV'