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
