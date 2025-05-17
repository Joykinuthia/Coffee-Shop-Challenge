class Coffee:
    def __init__(self, name):
    #Initialize with a name (str, >=3 characters)
        self._name = None
        self.name = name
        self._orders = []

    @property
    def name(self):
    #Getting the coffee's name
        return self._name

    @name.setter
    def name(self, value):
    #Setting the coffee's name with validation, immutable
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Coffee name is immutable")
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value

    def orders(self):
        return self._orders

    def customers(self):
    #Returns unique list of customers who ordered this coffee
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
    #Returns the total number of orders for this coffee
        return len(self._orders)

    def average_price(self):
    #Returns the average price of orders for this coffee, or 0 if none
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)
        