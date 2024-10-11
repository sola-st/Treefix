from typing import Set, Tuple # pragma: no cover

Index = int # pragma: no cover
string = 'example string with various slices' # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_iter_fexpr_slices': lambda self, x: [(0, 4), (10, 14)], # pragma: no cover
    '_iter_nameescape_slices': lambda self, x: [(5, 9)] # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
illegal_indices: Set[Index] = set()
_l_(17907)
iterators = [
    self._iter_fexpr_slices(string),
    self._iter_nameescape_slices(string),
]
_l_(17908)
for it in iterators:
    _l_(17911)

    for begin, end in it:
        _l_(17910)

        illegal_indices.update(range(begin, end + 1))
        _l_(17909)
aux = illegal_indices
_l_(17912)
exit(aux)
