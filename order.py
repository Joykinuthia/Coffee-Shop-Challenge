class Order:
    def __init__(self, customer, coffee, price):
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