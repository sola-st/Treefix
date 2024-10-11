import numpy as np # pragma: no cover

def new_block(values, placement, ndim): # pragma: no cover
    return type('MockBlock', (object,), { # pragma: no cover
        'values': values, # pragma: no cover
        '_split': lambda self: [new_block(values[[i]], [p], ndim) for i, p in enumerate(placement)] # pragma: no cover
    })() # pragma: no cover
 # pragma: no cover
def assert_block_equal(a, b): # pragma: no cover
    assert (a.values == b.values).all(), 'Block values are not equal' # pragma: no cover
    assert a._split == b._split, 'Block split methods are not equal' # pragma: no cover

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
