class Person:

    def __init__(self, fname:str, mname:str=None, lname:str=None):
        self.fname = fname
        self.mname = mname
        self.lname = lname

    def full_name(self)-> str:
        full_name = self.fname
        if self.mname is not None:
            full_name = f" {full_name} + {self.mname}"
            if self.lname is not None:
                full_name = f"{full_name}  {self.lname}"
        return full_name
    

person=Person("Hana", "John", "Smith")
print(person.full_name)