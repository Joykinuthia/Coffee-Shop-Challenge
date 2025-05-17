from customer import Customer
from coffee import Coffee
from order import Order

def main():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    order1 = alice.create_order(latte, 5.0)
    order2 = alice.create_order(espresso, 3.0)
    order3 = bob.create_order(latte, 4.5)
    print(f"Alice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")
    print(f"Latte's num orders: {latte.num_orders()}")
    print(f"Latte's average price: {latte.average_price()}")
    aficionado = Customer.most_aficionado(latte)
    print(f"Latte's most aficionado: {aficionado.name if aficionado else None}")

if __name__ == "__main__":
    main()