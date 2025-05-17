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

def test_coffee_orders_and_customers():
    coffee = Coffee("Mocha")
    customer1 = Customer("Joy")
    customer2 = Customer("Liam")
    order1 = Order(customer1, coffee, 5.0)
    order2 = Order(customer2, coffee, 4.0)
    assert len(coffee.orders()) == 2
    assert len(coffee.customers()) == 2
    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()

