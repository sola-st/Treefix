import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import operator # pragma: no cover
import pytest # pragma: no cover
import numpy.testing as tm # pragma: no cover

NaT = pd.NaT # pragma: no cover
other = np.array([pd.NaT, pd.NaT]) # pragma: no cover
tm = type('Mock', (object,), {'assert_numpy_array_equal': staticmethod(lambda a, b: None)})() # pragma: no cover
operator = type('Mock', (object,), {'le': operator.le, 'lt': operator.lt, 'ge': operator.ge, 'gt': operator.gt})() # pragma: no cover
pytest = type('Mock', (object,), {'raises': staticmethod(lambda exc_type, match: (yield))})() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import operator # pragma: no cover
import pytest # pragma: no cover
import numpy.testing as nt # pragma: no cover

NaT = pd.NaT # pragma: no cover
other = np.array([NaT, NaT], dtype=object) # pragma: no cover
class Mockpytest:  # Mock object for pytest # pragma: no cover
    class raises:  # Mock raises method # pragma: no cover
        def __init__(self, exc_type, match=None): # pragma: no cover
            self.exc_type = exc_type # pragma: no cover
            self.match = match # pragma: no cover
            self.entered = False # pragma: no cover
        def __enter__(self): # pragma: no cover
            self.entered = True # pragma: no cover
            return self # pragma: no cover
        def __exit__(self, exc_type, exc_val, exc_tb): # pragma: no cover
            assert not self.match or self.match in str(exc_val) # pragma: no cover
            return isinstance(exc_val, self.exc_type) # pragma: no cover
pytest = Mockpytest() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# GH#40722
from l3.Runtime import _l_
expected = np.array([False, False])
_l_(5733)
result = NaT == other
_l_(5734)
tm.assert_numpy_array_equal(result, expected)
_l_(5735)
result = other == NaT
_l_(5736)
tm.assert_numpy_array_equal(result, expected)
_l_(5737)

expected = np.array([True, True])
_l_(5738)
result = NaT != other
_l_(5739)
tm.assert_numpy_array_equal(result, expected)
_l_(5740)
result = other != NaT
_l_(5741)
tm.assert_numpy_array_equal(result, expected)
_l_(5742)

for symbol, op in [
    ("<=", operator.le),
    ("<", operator.lt),
    (">=", operator.ge),
    (">", operator.gt),
]:
    _l_(5750)

    msg = f"'{symbol}' not supported between"
    _l_(5743)

    with pytest.raises(TypeError, match=msg):
        _l_(5745)

        op(NaT, other)
        _l_(5744)

    if other.dtype == np.dtype("object"):
        _l_(5747)

        # uses the reverse operator, so symbol changes
        msg = None
        _l_(5746)
    with pytest.raises(TypeError, match=msg):
        _l_(5749)

        op(other, NaT)
        _l_(5748)
