# Extracted from https://stackoverflow.com/questions/222877/what-does-super-do-in-python-difference-between-super-init-and-expl
class SuperObject:        
    def __init__(self, **kwargs):
        print('SuperObject')
        mro = type(self).__mro__
        assert mro[-1] is object
        if mro[-2] is not SuperObject:
            raise TypeError(
                'all top-level classes in this hierarchy must inherit from SuperObject',
                'the last class in the MRO should be SuperObject',
                f'mro={[cls.__name__ for cls in mro]}'
            )

        # super().__init__ is guaranteed to be object.__init__        
        init = super().__init__
        init()

class A(SuperObject):
    def __init__(self, **kwargs):
        print("A")
        super(A, self).__init__(**kwargs)

class B(SuperObject):
    def __init__(self, **kwargs):
        print("B")
        super(B, self).__init__(**kwargs)

class C(A):
    def __init__(self, age, **kwargs):
        print("C",f"age={age}")
        super(C, self).__init__(age=age, **kwargs)

class D(B):
    def __init__(self, name, **kwargs):
        print("D", f"name={name}")
        super(D, self).__init__(name=name, **kwargs)

class E(C,D):
    def __init__(self, name, age, *args, **kwargs):
        print( "E", f"name={name}", f"age={age}")
        super(E, self).__init__(name=name, age=age, *args, **kwargs)

E(name='python', age=28)

E name=python age=28
C age=28
A
D name=python
B
SuperObject

