_ = 0 # pragma: no cover
def do_something(): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
from l3.Runtime import _l_
10 
_l_(927) 
10
_l_(928)

_ 
_l_(929) 
10
_l_(930)

_ * 3 
_l_(931) 
30
_l_(932)

x, _, y = (1, 2, 3)
_l_(933)

x
_l_(934)
1
_l_(935)

y 
_l_(936) 
3
_l_(937)

for _ in range(10):
    _l_(939)

    do_something()
    _l_(938)

