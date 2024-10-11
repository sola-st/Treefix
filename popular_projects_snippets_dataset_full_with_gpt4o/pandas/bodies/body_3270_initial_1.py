import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
import pandas._testing as tm # pragma: no cover

unit = 'D' # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
tm.assert_frame_equal = type('Mock', (object,), {'assert_frame_equal': lambda x, y: None}).assert_frame_equal # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# preserver the timedelta conversion
# GH#19223
from l3.Runtime import _l_
dtype = f"m8[{unit}]"
_l_(21018)
arr = np.array([[1, 2, 3]], dtype=dtype)
_l_(21019)
df = DataFrame(arr)
_l_(21020)
result = df.astype(dtype)
_l_(21021)
expected = DataFrame(arr.astype(dtype))
_l_(21022)

tm.assert_frame_equal(result, expected)
_l_(21023)
