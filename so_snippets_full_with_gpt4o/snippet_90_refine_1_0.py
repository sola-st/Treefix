from typing import Union # pragma: no cover

foo = [1, 3.14] # pragma: no cover

from typing import Union, List # pragma: no cover
import sys # pragma: no cover
import types # pragma: no cover

mock_typeguard = types.ModuleType('typeguard') # pragma: no cover
def mock_check_type(argname, value, expected_type): # pragma: no cover
    if not isinstance(value, expected_type.__origin__): # pragma: no cover
        raise TypeError(f"Expected {argname} to be of type {expected_type.__origin__}") # pragma: no cover
mock_typeguard.check_type = mock_check_type # pragma: no cover
sys.modules['typeguard'] = mock_typeguard # pragma: no cover
foo = [1, 3.14] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
from l3.Runtime import _l_
try:
    from typeguard import check_type
    _l_(14335)

except ImportError:
    pass
try:
    from typing import List
    _l_(14337)

except ImportError:
    pass

try:
    _l_(14341)

    check_type('mylist', [1, 2], List[int])
    _l_(14338)
except TypeError as e:
    _l_(14340)

    print(e)
    _l_(14339)

check_type('foo', [1, 3.14], List[Union[int, float]])
_l_(14342)
# vs
isinstance(foo, list) and all(isinstance(a, (int, float)) for a in foo) 
_l_(14343) 

