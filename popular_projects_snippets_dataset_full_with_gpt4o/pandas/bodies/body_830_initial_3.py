import numpy as np # pragma: no cover

def new_block(values, placement, ndim): # pragma: no cover
    class Block: # pragma: no cover
        def __init__(self, values, placement, ndim): # pragma: no cover
            self.values = values # pragma: no cover
            self.placement = placement # pragma: no cover
            self.ndim = ndim # pragma: no cover
        def _split(self): # pragma: no cover
            return [Block(self.values[[i]], [p], self.ndim) for i, p in enumerate(self.placement)] # pragma: no cover
    return Block(values, placement, ndim) # pragma: no cover
 # pragma: no cover
def assert_block_equal(res, exp): # pragma: no cover
    assert np.array_equal(res.values, exp.values) and res.placement == exp.placement and res.ndim == exp.ndim # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# GH#37799
from l3.Runtime import _l_
values = np.random.randn(3, 4)
_l_(17744)
blk = new_block(values, placement=[3, 1, 6], ndim=2)
_l_(17745)
result = blk._split()
_l_(17746)

# check that we get views, not copies
values[:] = -9999
_l_(17747)
assert (blk.values == -9999).all()
_l_(17748)

assert len(result) == 3
_l_(17749)
expected = [
    new_block(values[[0]], placement=[3], ndim=2),
    new_block(values[[1]], placement=[1], ndim=2),
    new_block(values[[2]], placement=[6], ndim=2),
]
_l_(17750)
for res, exp in zip(result, expected):
    _l_(17752)

    assert_block_equal(res, exp)
    _l_(17751)
