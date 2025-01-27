# Extracted from https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
  A    B
   \  /
    AB

class A():
    def __init__(self, a="a"):
        self.a = a
        print(f"a={a}")
    
    def A_method(self):
        print(f"A_method: {self.a}")

class B():
    def __init__(self, b="b"):
        self.b = b
        print(f"b={b}")
    
    def B_method(self):
        print(f"B_method: {self.b}")
    
    def magical_AB_method(self):
        print(f"magical_AB_method: {self.a}, {self.b}")

class AB(A,B):
    def __init__(self, a="A", b="B"):
        # super().__init__(a=a, b=b) # fails!
        A.__init__(self, a=a)
        B.__init__(self, b=b)
        self.A_method()
        self.B_method()
        self.magical_AB_method()


A()
a=a

B()
b=b

AB()
a=A
b=B
A_method: A
B_method: B

B().magical_AB_method()
AttributeError: 'B' object has no attribute 'a'

AB().magical_AB_method()
magical_AB_method: A, B

