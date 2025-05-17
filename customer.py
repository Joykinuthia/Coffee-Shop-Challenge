class Customer:
    def __init__(self, name):
        self.name = name
        self._orders =[]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders
    
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        from coffee import Coffee
        from order import Order
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
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
        