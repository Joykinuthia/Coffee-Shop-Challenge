import pytest
from coffee import Coffee

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("Ab")
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"
    with pytest.raises(AttributeError):
        coffee.name= "Mocha"

