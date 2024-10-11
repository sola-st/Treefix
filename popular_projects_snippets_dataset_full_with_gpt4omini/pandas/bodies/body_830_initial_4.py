import numpy as np # pragma: no cover

assert_block_equal = lambda block1, block2: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# GH#37799
from l3.Runtime import _l_
values = np.random.randn(3, 4)
_l_(5724)
blk = new_block(values, placement=[3, 1, 6], ndim=2)
_l_(5725)
result = blk._split()
_l_(5726)

# check that we get views, not copies
values[:] = -9999
_l_(5727)
assert (blk.values == -9999).all()
_l_(5728)

assert len(result) == 3
_l_(5729)
expected = [
    new_block(values[[0]], placement=[3], ndim=2),
    new_block(values[[1]], placement=[1], ndim=2),
    new_block(values[[2]], placement=[6], ndim=2),
]
_l_(5730)
for res, exp in zip(result, expected):
    _l_(5732)

    assert_block_equal(res, exp)
    _l_(5731)
