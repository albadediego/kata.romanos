from romano_class import NumeroRomano

def test_suma_romanos():
    nr1 = NumeroRomano("XX")
    nr2 = NumeroRomano(30)

    nr3 = nr1 + nr2

    assert isinstance(nr3, NumeroRomano) == True
    assert nr3.valor_numerico == 50
    assert nr3.valor_romano == 'L'