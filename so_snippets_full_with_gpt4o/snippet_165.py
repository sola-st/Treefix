# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-the-self-parameter-why-is-it-needed
from l3.Runtime import _l_
class C:
    _l_(14140)

    def m1(self, arg):
        _l_(14139)

        print(self, ' inside')
        _l_(14137)
        pass
        _l_(14138)

ci =C()
_l_(14141)
print(ci, ' outside')
_l_(14142)
ci.m1(None)
_l_(14143)
print(hex(id(ci))) # hex memory address
_l_(14144) # hex memory address

0x2b9d79c6cc0
_l_(14145)

