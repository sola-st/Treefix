import numpy as np # pragma: no cover
import pytest # pragma: no cover

data = np.array([1, 2, 3]) # pragma: no cover

import numpy as np # pragma: no cover
import pytest # pragma: no cover

data = np.array([1, 2, 3]) # pragma: no cover
class MockSelf:# pragma: no cover
    def assert_extension_array_equal(self, a, b):# pragma: no cover
        assert (a == b).all() # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
from l3.Runtime import _l_
arr2d = data.reshape(1, -1)
_l_(22217)

result = arr2d[0]
_l_(22218)
self.assert_extension_array_equal(result, data)
_l_(22219)

with pytest.raises(IndexError):
    _l_(22221)

    arr2d[1]
    _l_(22220)

with pytest.raises(IndexError):
    _l_(22223)

    arr2d[-2]
    _l_(22222)

result = arr2d[:]
_l_(22224)
self.assert_extension_array_equal(result, arr2d)
_l_(22225)

result = arr2d[:, :]
_l_(22226)
self.assert_extension_array_equal(result, arr2d)
_l_(22227)

result = arr2d[:, 0]
_l_(22228)
expected = data[[0]]
_l_(22229)
self.assert_extension_array_equal(result, expected)
_l_(22230)

# dimension-expanding getitem on 1D
result = data[:, np.newaxis]
_l_(22231)
self.assert_extension_array_equal(result, arr2d.T)
_l_(22232)
