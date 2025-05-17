import pytest
from customer import Customer

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)
    customer = Customer("Joy")
    assert customer.name =="Joy"

def test_customer_orders_and_coffees():
    customer = Customer("Liam")
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Cortado")
    order1 = Order(customer, coffee1, 5.0)
    order2 = Order(customer, coffee2, 3.0)
    assert len(customer.orders()) == 2
    assert len(customer.coffees()) == 2
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

def test_create_order():
    customer = Customer("Charlie")
    coffee = Coffee("Mocha")
    order = customer.create_order(coffee, 4.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5
