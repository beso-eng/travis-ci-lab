# test_maths.py
import maths

def test_addition():
    assert maths.add(2, 3) == 5

def test_subtraction():
    assert maths.subtract(5, 3) == 2

def test_wrongsubtraction():
    assert maths.subtract(6, 4) == 2  

# Intentionally wrong on purpose (should fail)
def test_wrongmultiply():
    # our function is multiply, not mutiply; also 6*4 == 24
    assert maths.multiply(6, 4) == 2
