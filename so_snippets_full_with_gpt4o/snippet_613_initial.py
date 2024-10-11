# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3257919/what-is-the-difference-between-is-none-and-none
from l3.Runtime import _l_
p = [1]
_l_(12476)
q = [1]
_l_(12477)
p is q # False because they are not the same actual object
_l_(12478) # False because they are not the same actual object
p == q # True because they are equivalent
_l_(12479) # True because they are equivalent

p = None
_l_(12480)
q = None
_l_(12481)
p is q # True because they are both pointing to the same "None"
_l_(12482) # True because they are both pointing to the same "None"

