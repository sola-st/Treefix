import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pytest # pragma: no cover

Series = pd.Series # pragma: no cover
pytest.raises = type('Mock', (object,), {'raises': staticmethod(lambda exception, match: None)}) # pragma: no cover
np.arange = staticmethod(lambda x: list(range(x))) # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pytest # pragma: no cover

Series = pd.Series # pragma: no cover
np.arange = lambda x: list(range(x)) # pragma: no cover
pytest.raises = lambda exception, match: (lambda func: func)  # mock the function to do nothing # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# shift requires scalar fill_value except for object dtype
from l3.Runtime import _l_
ser = Series(range(3))
_l_(8754)
with pytest.raises(ValueError, match="fill_value must be a scalar"):
    _l_(8756)

    ser.shift(1, fill_value=[])
    _l_(8755)

df = ser.to_frame()
_l_(8757)
with pytest.raises(ValueError, match="fill_value must be a scalar"):
    _l_(8759)

    df.shift(1, fill_value=np.arange(3))
    _l_(8758)

obj_ser = ser.astype(object)
_l_(8760)
result = obj_ser.shift(1, fill_value={})
_l_(8761)
assert result[0] == {}
_l_(8762)

obj_df = obj_ser.to_frame()
_l_(8763)
result = obj_df.shift(1, fill_value={})
_l_(8764)
assert result.iloc[0, 0] == {}
_l_(8765)
