from customer import Customer
from coffee import Coffee
from order import Order

def main():
    joy = Customer("Joy")
    liam = Customer("Liam")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    order1 = joy.create_order(latte, 5.0)
    order2 = joy.create_order(espresso, 3.0)
    order3 = liam.create_order(latte, 4.5)
    print(f"Joy's orders: {len(joy.orders())}")
    print(f"Joy's coffees: {[coffee.name for coffee in joy.coffees()]}")
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")
    print(f"Latte's num orders: {latte.num_orders()}")
    print(f"Latte's average price: {latte.average_price()}")
    aficionado = Customer.most_aficionado(latte)
    print(f"Latte's most aficionado: {aficionado.name if aficionado else None}")

if __name__ == "__main__":
    main()