import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("Ab")
    coffee = Coffee("Americano")
    assert coffee.name == "Americano"
    with pytest.raises(AttributeError):
        coffee.name = "Latte"

def test_coffee_orders_and_customers():
    coffee = Coffee("Latte")
    customer1 = Customer("Joy")
    customer2 = Customer("Liam")
    order1 = Order(customer1, coffee, 5.0)
    order2 = Order(customer2, coffee, 4.0)
    assert len(coffee.orders()) == 2
    assert len(coffee.customers()) == 2
    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()

def test_num_orders_and_average_price():
    coffee = Coffee("Espresso")
    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0
    customer = Customer("Brad")
    Order(customer, coffee, 3.0)
    Order(customer, coffee, 5.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.0