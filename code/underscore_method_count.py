class UnderscoreMeta(type):
    """
    Metaclass that ensures all attributes of a class start with an underscore.
    """
    def __new__(cls, name, bases, dct):
        """
        Override __new__ method to modify class attributes.
        """
        for key, value in dct.items():
            if not key.startswith('_'):
                dct['_' + key] = value
                del dct[key]
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=UnderscoreMeta):
    """
    Example class using UnderscoreMeta metaclass.
    """
    x = 10
    y = 20

obj = MyClass()
print(obj._x)  # Output: 10
print(obj._y)  # Output: 20
