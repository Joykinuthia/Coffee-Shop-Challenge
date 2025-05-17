class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance")