class Order:
    def __init__(self, customer, coffee, price):
    #Initialize with customer, coffee, and price (float, 1.0-10.0)
        from customer import Customer
        from coffee import Coffee
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._customer = customer
        self._coffee = coffee
        self._price = None
        self.price = price
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def price(self):
    #Getting the order's price
        return self._price

    @price.setter
    def price(self, value):
    #Setting the order's price with validation, immutable once set
        if hasattr(self, '_price') and self._price is not None:
            raise AttributeError("Price is immutable")
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

