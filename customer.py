class Customer:
    def __init__(self, name):
    #Initialize a name (str, 1-15 characters)
        self.name = name
        self._orders = []

    @property
    def name(self):
    #Getting the customer's name
        return self._name

    @name.setter
    def name(self, value):
    #Setting the customer's name with validation
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
    #Returns unique list of coffees ordered by the customer
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
    #Creates a new order for the customer with given coffee and price
        from coffee import Coffee
        from order import Order
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
    #Returns the customer who spent the most on the given coffee, or None if no orders
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        if not coffee.orders():
            return None
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price
        return max(customer_spending, key=customer_spending.get)
        