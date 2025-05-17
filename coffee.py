class Coffee:
    def __init__(self, name):
        self.name = name
        self._name = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "_name") and self._name is not None:
            raise AttributeError("Coffee name is immutable")
        if not isinstance(value,str):
            raise TypeError("Name must be a string")
        if len(value) <3:
            raise ValueError("Name must be at least 3 characters")
        self._name = value
        