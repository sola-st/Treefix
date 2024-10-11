from typing import Set, Tuple, Iterator # pragma: no cover

string = 'example string' # pragma: no cover
Set = set # pragma: no cover
Index = int # pragma: no cover
self = type('Mock', (object,), { '_iter_fexpr_slices': lambda s: iter([(0, 5), (10, 15)]), '_iter_nameescape_slices': lambda s: iter([(6, 9)])})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
illegal_indices: Set[Index] = set()
_l_(6180)
iterators = [
    self._iter_fexpr_slices(string),
    self._iter_nameescape_slices(string),
]
_l_(6181)
for it in iterators:
    _l_(6184)

    for begin, end in it:
        _l_(6183)

        illegal_indices.update(range(begin, end + 1))
        _l_(6182)
aux = illegal_indices
_l_(6185)
exit(aux)
