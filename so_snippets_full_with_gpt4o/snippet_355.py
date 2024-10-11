# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
from l3.Runtime import _l_
10 
_l_(12892) 
10
_l_(12893)

_ 
_l_(12894) 
10
_l_(12895)

_ * 3 
_l_(12896) 
30
_l_(12897)

x, _, y = (1, 2, 3)
_l_(12898)

x
_l_(12899)
1
_l_(12900)

y 
_l_(12901) 
3
_l_(12902)

for _ in range(10):
    _l_(12904)

    do_something()
    _l_(12903)

