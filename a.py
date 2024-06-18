# a.py

from b import B

class A:
    def __init__(self):
        self.b = B()
        print("A is initialized")

    def show(self):
        print("This is class A")
