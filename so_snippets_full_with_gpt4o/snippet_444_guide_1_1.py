import sys # pragma: no cover
import types # pragma: no cover

sys.modules['more_itertools'] = types.ModuleType('more_itertools'); sys.modules['more_itertools'].chunked = lambda iterable, n: [list(iterable[i:i + n]) for i in range(0, len(iterable), n)] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
from l3.Runtime import _l_
try:
    import more_itertools
    _l_(14963)

except ImportError:
    pass
for s in more_itertools.chunked(range(9), 4):
    _l_(14965)

    print(s)
    _l_(14964)

[0, 1, 2, 3]
_l_(14966)
[4, 5, 6, 7]
_l_(14967)
[8]
_l_(14968)

