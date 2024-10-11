# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1261875/what-does-nonlocal-do-in-python-3
from l3.Runtime import _l_
a = 10
_l_(12603)
def Outer(msg):
    _l_(12617)

    a = 20
    _l_(12604)
    b = 30
    _l_(12605)
    def Inner():
        _l_(12614)

        c = 50
        _l_(12606)
        d = 60
        _l_(12607)
        print("MU LCL =",locals())
        _l_(12608)
        nonlocal a
        _l_(12609)
        a = 100
        _l_(12610)
        ans = a+c
        _l_(12611)
        print("Hello from Inner",ans)       
        _l_(12612)       
        print("value of a Inner : ",a)
        _l_(12613)
    Inner()
    _l_(12615)
    print("value of a Outer : ",a)
    _l_(12616)

res = Outer("Hello World")
_l_(12618)
print(res)
_l_(12619)
print("value of a Global : ",a)
_l_(12620)

