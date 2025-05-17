import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    customer = Customer("Joy")
    coffee = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)
    with pytest.raises(TypeError):
        Order(customer, "not a coffee", 5.0)
    with pytest.raises(TypeError):
        Order(customer, coffee, "5.0")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    with pytest.raises(AttributeError):
        order.price = 6.0