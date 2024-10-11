from typing import List, Union # pragma: no cover

foo = [1, 2.5] # pragma: no cover
Union = type('Union', (), {}) # pragma: no cover

from typing import List, Union # pragma: no cover

def check_type(name, value, expected): # pragma: no cover
    if not isinstance(value, expected): # pragma: no cover
        raise TypeError(f'Expected type {expected} for {name}, got {type(value)}') # pragma: no cover
foo = [1, 2.5] # pragma: no cover
Union = type('Union', (), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
from l3.Runtime import _l_
try:
    from typeguard import check_type
    _l_(2141)

except ImportError:
    pass
try:
    from typing import List
    _l_(2143)

except ImportError:
    pass

try:
    _l_(2147)

    check_type('mylist', [1, 2], List[int])
    _l_(2144)
except TypeError as e:
    _l_(2146)

    print(e)
    _l_(2145)

check_type('foo', [1, 3.14], List[Union[int, float]])
_l_(2148)
# vs
isinstance(foo, list) and all(isinstance(a, (int, float)) for a in foo) 
_l_(2149) 

