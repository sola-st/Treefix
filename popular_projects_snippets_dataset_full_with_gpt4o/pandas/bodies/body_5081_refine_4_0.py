import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import operator # pragma: no cover
import pytest # pragma: no cover
from pandas._libs.tslibs.nattype import NaTType # pragma: no cover
import pandas._testing as tm # pragma: no cover

NaT = pd.NaT # pragma: no cover
other = np.array([pd.NaT, pd.NaT], dtype='object') # pragma: no cover
other.dtype = np.dtype('object') # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import operator # pragma: no cover
import pytest # pragma: no cover
from pandas._libs.tslibs.nattype import NaTType # pragma: no cover
import pandas._testing as tm # pragma: no cover

NaT = pd.NaT # pragma: no cover
other = np.array([pd.Timestamp('2023-01-01'), pd.Timestamp('2023-01-02')]) # pragma: no cover
tm = type('Mock', (object,), {'assert_numpy_array_equal': staticmethod(tm.assert_numpy_array_equal)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# GH#40722
from l3.Runtime import _l_
expected = np.array([False, False])
_l_(17783)
result = NaT == other
_l_(17784)
tm.assert_numpy_array_equal(result, expected)
_l_(17785)
result = other == NaT
_l_(17786)
tm.assert_numpy_array_equal(result, expected)
_l_(17787)

expected = np.array([True, True])
_l_(17788)
result = NaT != other
_l_(17789)
tm.assert_numpy_array_equal(result, expected)
_l_(17790)
result = other != NaT
_l_(17791)
tm.assert_numpy_array_equal(result, expected)
_l_(17792)

for symbol, op in [
    ("<=", operator.le),
    ("<", operator.lt),
    (">=", operator.ge),
    (">", operator.gt),
]:
    _l_(17800)

    msg = f"'{symbol}' not supported between"
    _l_(17793)

    with pytest.raises(TypeError, match=msg):
        _l_(17795)

        op(NaT, other)
        _l_(17794)

    if other.dtype == np.dtype("object"):
        _l_(17797)

        # uses the reverse operator, so symbol changes
        msg = None
        _l_(17796)
    with pytest.raises(TypeError, match=msg):
        _l_(17799)

        op(other, NaT)
        _l_(17798)
