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
    coffee1 = Coffee("Americano")
    coffee2 = Coffee("Cortado")
    order1 = Order(customer, coffee1, 5.0)
    order2 = Order(customer, coffee2, 3.0)
    assert len(customer.orders()) == 2
    assert len(customer.coffees()) == 2
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()
