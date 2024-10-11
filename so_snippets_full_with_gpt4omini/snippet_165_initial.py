# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-the-self-parameter-why-is-it-needed
from l3.Runtime import _l_
class C:
    _l_(1617)

    def m1(self, arg):
        _l_(1616)

        print(self, ' inside')
        _l_(1614)
        pass
        _l_(1615)

ci =C()
_l_(1618)
print(ci, ' outside')
_l_(1619)
ci.m1(None)
_l_(1620)
print(hex(id(ci))) # hex memory address
_l_(1621) # hex memory address

0x2b9d79c6cc0
_l_(1622)

