import pandas as pd # pragma: no cover
import re # pragma: no cover
import numpy as np # pragma: no cover
from pandas.errors import PerformanceWarning # pragma: no cover

Series = pd.Series # pragma: no cover
any_string_dtype = 'string' # pragma: no cover
tm = type('Mock', (object,), {'maybe_produces_warning': staticmethod(lambda *args, **kwargs: args[0]), 'assert_series_equal': staticmethod(lambda left, right: None)})() # pragma: no cover
PerformanceWarning = PerformanceWarning # pragma: no cover

import pandas as pd # pragma: no cover
import re # pragma: no cover
import numpy as np # pragma: no cover
from pandas.errors import PerformanceWarning # pragma: no cover

Series = pd.Series # pragma: no cover
any_string_dtype = 'string' # pragma: no cover
class Mock: pass# pragma: no cover
 # pragma: no cover
def mock_maybe_produces_warning(*args, **kwargs): return args[0]# pragma: no cover
 # pragma: no cover
def mock_assert_series_equal(left, right): pass# pragma: no cover
 # pragma: no cover
tm = Mock()# pragma: no cover
 # pragma: no cover
tm.maybe_produces_warning = staticmethod(mock_maybe_produces_warning)# pragma: no cover
 # pragma: no cover
tm.assert_series_equal = staticmethod(mock_assert_series_equal)# pragma: no cover
 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
from l3.Runtime import _l_
ser = Series([b"abcd,\xc3\xa0".decode("utf-8")], dtype=any_string_dtype)
_l_(10412)
expected = Series([b"abcd, \xc3\xa0".decode("utf-8")], dtype=any_string_dtype)
_l_(10413)
pat = re.compile(r"(?<=\w),(?=\w)", flags=re.UNICODE)
_l_(10414)
with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    _l_(10416)

    result = ser.str.replace(pat, ", ", regex=True)
    _l_(10415)
tm.assert_series_equal(result, expected)
_l_(10417)
