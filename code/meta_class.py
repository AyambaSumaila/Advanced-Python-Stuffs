#Question 3: Implement a metaclass that logs the creation of instances of its subclasses.

class LoggingMeta(type):
    """
    Metaclass that logs the creation of instances of its subclasses.
    """
    def __new__(cls, name, bases, dct):
        """
        Override __new__ method to initialize instance counter.
        """
        cls_obj = super().__new__(cls, name, bases, dct)
        cls_obj._instances_created = 0
        return cls_obj

    def __call__(cls, *args, **kwargs):
        """
        Override __call__ method to log instance creation.
        """
        instance = super().__call__(*args, **kwargs)
        cls._instances_created += 1
        print(f"Instance of {cls.__name__} created. Total instances: {cls._instances_created}")
        return instance

class MyClass(metaclass=LoggingMeta):
    """
    Example class using LoggingMeta metaclass.
    """
    pass

obj1 = MyClass()
obj2 = MyClass()
