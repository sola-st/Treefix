import pandas as pd # pragma: no cover
import re # pragma: no cover
import pandas.testing as tm # pragma: no cover
from pandas import StringDtype # pragma: no cover
from pandas.errors import PerformanceWarning # pragma: no cover

Series = pd.Series # pragma: no cover
any_string_dtype = StringDtype() # pragma: no cover
tm.maybe_produces_warning = type('Mock', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_val, exc_tb: None}) # pragma: no cover
tm.assert_series_equal = tm.assert_series_equal # pragma: no cover

import pandas as pd # pragma: no cover
import re # pragma: no cover
import pandas.testing as tm # pragma: no cover
from pandas import StringDtype # pragma: no cover
from pandas.errors import PerformanceWarning # pragma: no cover

Series = pd.Series # pragma: no cover
any_string_dtype = StringDtype() # pragma: no cover
tm.maybe_produces_warning = type('MockContextManager', (object,), {'__init__': lambda self, *args, **kwargs: None, '__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_val, exc_tb: None}) # pragma: no cover
tm.assert_series_equal = tm.assert_series_equal # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
from l3.Runtime import _l_
ser = Series([b"abcd,\xc3\xa0".decode("utf-8")], dtype=any_string_dtype)
_l_(21201)
expected = Series([b"abcd, \xc3\xa0".decode("utf-8")], dtype=any_string_dtype)
_l_(21202)
pat = re.compile(r"(?<=\w),(?=\w)", flags=re.UNICODE)
_l_(21203)
with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    _l_(21205)

    result = ser.str.replace(pat, ", ", regex=True)
    _l_(21204)
tm.assert_series_equal(result, expected)
_l_(21206)
