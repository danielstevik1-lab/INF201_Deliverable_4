import pytest
from fraction import Fraction

def test_initialization_and_simplification():
    #this will test the proper initialisation and other stuff
    f = Fraction(2, 4)
    assert f.numerator == 1
    assert f.denominator == 2

    f_default = Fraction(5)
    assert f_default.numerator == 5
    assert f_default.denominator == 1

def test_validation():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)
    with pytest.raises(TypeError):
        Fraction(1, "2")
    with pytest.raises(TypeError):
        Fraction(True, 2)
    with pytest.raises(ValueError):
        Fraction(1, 0)
    with pytest.raises(ValueError):
        Fraction(1, -5)

def test_read_only():
    f = Fraction(1, 3)
    with pytest.raises(AttributeError):
        f.numerator = 2
    with pytest.raises(AttributeError):
        f.denominator = 4

def test_arithmetic_and_conversion():
    f1 = Fraction(1,2)
    f2 = Fraction(1, 3)

    assert f1 + f2 == Fraction(5,6)
    assert f1 - f2 == Fraction(1,6)
    assert f1 * f2 == Fraction(1,6)
    assert f1 / f2 == Fraction(3,2)
    assert -f1 == Fraction(-1,2)
    assert float(f1) == 0.5

def test_division_by_zero():
    f1 = Fraction(1, 2)
    with pytest.raises(ZeroDivisionError):
        _ = f1 / Fraction(0)

def test_string_representation():
    f1 = Fraction(3, 4)
    f2 = Fraction(6, 2)
    assert repr(f1) == "Fraction(3, 4)"
    assert str(f1) == "3/4"
    assert str(f2) == "3"

def test_comparisons():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    f3 = Fraction(3, 4)
    f_neg = Fraction(-1, 2)

    assert f1 == f2
    assert f1 != f3
    assert f_neg < f1
    assert f1 < f3
    assert f1 <= f2
    assert f1 <= f3
    assert f3 > f1
    assert f3 >= f1
    assert f2 >= f1

    #non fraction comparisons should yield us return notimplemented
    assert (f1 == 0.5) is False
    with pytest.raises(TypeError):
        _ = f1 < 1
