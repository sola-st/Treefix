import numpy as np # pragma: no cover
import pytest # pragma: no cover

data = np.array([1, 2, 3]) # pragma: no cover
self = type('Mock', (object,), {'assert_extension_array_equal': lambda x, y: np.array_equal(x, y)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
from l3.Runtime import _l_
arr2d = data.reshape(1, -1)
_l_(10655)

result = arr2d[0]
_l_(10656)
self.assert_extension_array_equal(result, data)
_l_(10657)

with pytest.raises(IndexError):
    _l_(10659)

    arr2d[1]
    _l_(10658)

with pytest.raises(IndexError):
    _l_(10661)

    arr2d[-2]
    _l_(10660)

result = arr2d[:]
_l_(10662)
self.assert_extension_array_equal(result, arr2d)
_l_(10663)

result = arr2d[:, :]
_l_(10664)
self.assert_extension_array_equal(result, arr2d)
_l_(10665)

result = arr2d[:, 0]
_l_(10666)
expected = data[[0]]
_l_(10667)
self.assert_extension_array_equal(result, expected)
_l_(10668)

# dimension-expanding getitem on 1D
result = data[:, np.newaxis]
_l_(10669)
self.assert_extension_array_equal(result, arr2d.T)
_l_(10670)
