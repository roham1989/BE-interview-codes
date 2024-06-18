# b.py

from a import A

class B:
    def __init__(self):
        self.a = A()
        print("B is initialized")

    def display(self):
        print("This is class B")

