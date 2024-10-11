w = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
from l3.Runtime import _l_
def somefunction(p):
    _l_(1504)

    a=p+1
    _l_(1500)
    b=p+2
    _l_(1501)
    c=-p
    _l_(1502)
    aux = a, b, c
    _l_(1503)
    return aux

x, y, z = somefunction(w)
_l_(1505)

def somefunction(a, b, c):
    _l_(1510)

    a = a * 2
    _l_(1506)
    b = b + a
    _l_(1507)
    c = a * b * c
    _l_(1508)
    aux = a, b, c
    _l_(1509)
    return aux

x = 3
_l_(1511)
y = 5
_l_(1512)
z = 10
_l_(1513)
print(F"Before : {x}, {y}, {z}")
_l_(1514)

x, y, z = somefunction(x, y, z)
_l_(1515)

print(F"After  : {x}, {y}, {z}")
_l_(1516)

