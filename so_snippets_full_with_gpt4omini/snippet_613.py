# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3257919/what-is-the-difference-between-is-none-and-none
from l3.Runtime import _l_
p = [1]
_l_(632)
q = [1]
_l_(633)
p is q # False because they are not the same actual object
_l_(634) # False because they are not the same actual object
p == q # True because they are equivalent
_l_(635) # True because they are equivalent

p = None
_l_(636)
q = None
_l_(637)
p is q # True because they are both pointing to the same "None"
_l_(638) # True because they are both pointing to the same "None"

