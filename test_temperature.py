import pytest
from temperature_conversion import Temperature

""" ----- Testing: point 1 -> Initialization -----"""
def test_CaseInsensitivity():
    """ Tests case sensitivity"""
    t1= Temperature(25, "C")
    t2= Temperature(25, "c")

    assert t1 == t2

def test_ReadOnly():
    """ Tests read only attributes"""
    temp = Temperature(25, "c")

    with pytest.raises(AttributeError):
        temp.value = 100

    with pytest.raises(AttributeError):
        temp.unit = "k"

""" ----- Testing: point 2 -> Validation -----"""
def test_InvalidUnit():
    """Tests if class only accepts valid units"""
    with pytest.raises(ValueError):
        Temperature(25, "kroner")

def test_AbsoluteZeroCelsius():
    """Tests if Celsius can go below absolute zero"""
    with pytest.raises(ValueError):
        Temperature(-273.2, "c")

def test_AbsoluteZeroFahrenheit():
    """Tests if Fahrenheit can go below absolute zero"""
    with pytest.raises(ValueError):
        Temperature(-470, "f")

def test_AbsoluteZeroKelvin():
    """Tests if Kelvin can go below absolute zero""" 
    with pytest.raises(ValueError):
        Temperature(-0.1, "k")

""" ----- Testing: point 3 -> Conversions -----"""
def test_AbsoluteZero():
    """Tests if converting is correct at absolute zero"""
    assert Temperature(-273.15, "c") == Temperature(-459.67, "f")
    assert Temperature(-273.15, "c") == Temperature(0, "k")

def test_CelsiusFahrenheitCrossover():
    """Tests if converting is correct at celsius/fahrenheit intercection"""
    assert Temperature(-40, "c") == Temperature(-40, "f")
    assert Temperature(-40, "c") == Temperature(233.15, "k")

def test_FreezingWater():
    """Tests if converting is corrext at 0C"""
    assert Temperature(0,"c") == Temperature(32,"f")
    assert Temperature(0, "c") == Temperature(273.15,"k")

def test_HumanBody():
    """Test if converting is correct at human temperature"""
    assert Temperature(37,"c") == Temperature(98.6,"f")
    assert Temperature(37,"c") == Temperature(310.15,"k")

def test_BoilingWater():
    """Test if converting is correct at water boil point"""
    assert Temperature(100,"c") == Temperature(212,"f")
    assert Temperature(100,"c") == Temperature(373.15,"k")

""" ----- Testing: point 4 -> Round-trip Conversions -----"""
def test_RoundTrip():
    """Tests if original temperature is maintained after converting through all three units"""
    test_temp = Temperature(32, "c")
    control_temp = (test_temp.convert_to("f").convert_to("k").convert_to("c"))

    assert test_temp == control_temp

""" ----- Testing: point 5 -> Cross-unit Comparisons -----"""
def test_Equal():
    """Test ' is equal' operator"""
    assert Temperature(0,"c") == Temperature(32, "f")

def test_Less():
    """Test 'less than' operator"""
    assert Temperature(0, "c") < Temperature(45, "f")

def test_LessOrEqual():
    """Test 'less or equal than' operator"""
    assert Temperature(0, "c") <= Temperature(273.15, "k")

def test_Greater():
    """Test 'greater than' operator"""
    assert Temperature(0,"c") > Temperature(28, "f")


def test_GreaterOrEqual():
    """Test 'greater or equal than' operator"""
    assert Temperature(0,"c") >= Temperature(273.15, "k")


""" ----- Testing: point 6 -> String formatting-----"""
def test_repr():
    """Test repr method"""
    temp = Temperature(25, "c")

    assert repr(temp) == "Temperature(25.0,'c')"
