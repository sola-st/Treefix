import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import numpy as np # pragma: no cover

Series = pd.Series # pragma: no cover
pytest.raises = type('Mock', (object,), {'__call__': lambda self, *args, **kwargs: pytest.raises(*args, **kwargs)}) # pragma: no cover
np.arange = np.arange # pragma: no cover

import pandas as pd # pragma: no cover
import pytest # pragma: no cover
import numpy as np # pragma: no cover

Series = pd.Series # pragma: no cover
pytest.raises = type('Mock', (object,), {'__call__': lambda self, exc_type, *, match: pytest.raises(exc_type, match=match)}) # pragma: no cover
np.arange = np.arange # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# shift requires scalar fill_value except for object dtype
from l3.Runtime import _l_
ser = Series(range(3))
_l_(20338)
with pytest.raises(ValueError, match="fill_value must be a scalar"):
    _l_(20340)

    ser.shift(1, fill_value=[])
    _l_(20339)

df = ser.to_frame()
_l_(20341)
with pytest.raises(ValueError, match="fill_value must be a scalar"):
    _l_(20343)

    df.shift(1, fill_value=np.arange(3))
    _l_(20342)

obj_ser = ser.astype(object)
_l_(20344)
result = obj_ser.shift(1, fill_value={})
_l_(20345)
assert result[0] == {}
_l_(20346)

obj_df = obj_ser.to_frame()
_l_(20347)
result = obj_df.shift(1, fill_value={})
_l_(20348)
assert result.iloc[0, 0] == {}
_l_(20349)
