w = 4 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
from l3.Runtime import _l_
def somefunction(p):
    _l_(13512)

    a=p+1
    _l_(13508)
    b=p+2
    _l_(13509)
    c=-p
    _l_(13510)
    aux = a, b, c
    _l_(13511)
    return aux

x, y, z = somefunction(w)
_l_(13513)

def somefunction(a, b, c):
    _l_(13518)

    a = a * 2
    _l_(13514)
    b = b + a
    _l_(13515)
    c = a * b * c
    _l_(13516)
    aux = a, b, c
    _l_(13517)
    return aux

x = 3
_l_(13519)
y = 5
_l_(13520)
z = 10
_l_(13521)
print(F"Before : {x}, {y}, {z}")
_l_(13522)

x, y, z = somefunction(x, y, z)
_l_(13523)

print(F"After  : {x}, {y}, {z}")
_l_(13524)

