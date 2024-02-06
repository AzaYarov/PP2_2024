class ParentClass:
    def __init__(self):
        print("ParentClass constructor")

    def some_method(self):
        print("ParentClass method")


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Calls the constructor of the parent class
        print("ChildClass constructor")

    def some_method(self):
        super().some_method()  # Calls the method of the parent class
        print("ChildClass method")


child = ChildClass()
child.some_method()
