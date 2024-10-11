from unittest.mock import MagicMock # pragma: no cover

more_itertools = MagicMock() # pragma: no cover
more_itertools.chunked = MagicMock(return_value=[[0, 1, 2, 3], [4, 5, 6, 7], [8]]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
from l3.Runtime import _l_
try:
    import more_itertools
    _l_(2446)

except ImportError:
    pass
for s in more_itertools.chunked(range(9), 4):
    _l_(2448)

    print(s)
    _l_(2447)

[0, 1, 2, 3]
_l_(2449)
[4, 5, 6, 7]
_l_(2450)
[8]
_l_(2451)

