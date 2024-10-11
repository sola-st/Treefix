import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

Series = pd.Series # pragma: no cover
get_groupby_method_args = lambda func, ser: () # pragma: no cover
transformation_func = 'cumcount' # pragma: no cover
dropna = True # pragma: no cover
concat = pd.concat # pragma: no cover
tm = type('Mock', (object,), {'assert_produces_warning': lambda self, *args: None, 'assert_equal': lambda self, left, right: None})() # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover
import pandas.testing as tm # pragma: no cover

Series = pd.Series # pragma: no cover
get_groupby_method_args = lambda func, ser: () # pragma: no cover
transformation_func = 'cumcount' # pragma: no cover
dropna = True # pragma: no cover
concat = pd.concat # pragma: no cover
class Mock:  # Custom mock class to simulate behavior of `tm` # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_produces_warning(*args, **kwargs): pass # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_equal(left, right): pass # pragma: no cover
tm = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 17093
from l3.Runtime import _l_
ser = Series([1, 2, 2], index=[1, 2, 3])
_l_(9090)
args = get_groupby_method_args(transformation_func, ser)
_l_(9091)
gb = ser.groupby([1, 1, np.nan], dropna=dropna)
_l_(9092)

buffer = []
_l_(9093)
for k, (idx, group) in enumerate(gb):
    _l_(9100)

    if transformation_func == "cumcount":
        _l_(9098)

        # Series has no cumcount method
        res = Series(range(len(group)), index=group.index)
        _l_(9094)
    elif transformation_func == "ngroup":
        _l_(9097)

        res = Series(k, index=group.index)
        _l_(9095)
    else:
        res = getattr(group, transformation_func)(*args)
        _l_(9096)
    buffer.append(res)
    _l_(9099)
if dropna:
    _l_(9103)

    dtype = object if transformation_func in ("any", "all") else None
    _l_(9101)
    buffer.append(Series([np.nan], index=[3], dtype=dtype))
    _l_(9102)
expected = concat(buffer)
_l_(9104)

with tm.assert_produces_warning(None):
    _l_(9106)

    result = gb.transform(transformation_func, *args)
    _l_(9105)

tm.assert_equal(result, expected)
_l_(9107)
