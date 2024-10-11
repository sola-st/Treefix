import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover

Series = pd.Series # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# like test_setitem_mask_smallint_upcast, but while we can't hold 'alt',
#  we *can* hold alt[mask] without casting
from l3.Runtime import _l_
orig = Series([1, 2, 3], dtype="uint8")
_l_(21248)
alt = Series([245, 1000, 246], dtype=np.int64)
_l_(21249)

mask = np.array([True, False, True])
_l_(21250)

ser = orig.copy()
_l_(21251)
ser[mask] = alt
_l_(21252)
expected = Series([245, 2, 246], dtype="uint8")
_l_(21253)
tm.assert_series_equal(ser, expected)
_l_(21254)

ser2 = orig.copy()
_l_(21255)
ser2.mask(mask, alt, inplace=True)
_l_(21256)
tm.assert_series_equal(ser2, expected)
_l_(21257)
