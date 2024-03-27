#Question 2: Create a metaclass that counts the number of method definitions in a class.
class MethodCountMeta(type):
    """
    Metaclass that counts the number of method definitions in a class.
    """
    def __new__(cls, name, bases, dct):
        """
        Override __new__ method to count method definitions.
        """
        method_count = sum(1 for key, value in dct.items() if callable(value))
        dct['_method_count'] = method_count
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MethodCountMeta):
    """
    Example class using MethodCountMeta metaclass.
    """
    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass

print(MyClass._method_count)  # Output: 3
