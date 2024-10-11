import pandas as pd # pragma: no cover
import re # pragma: no cover
import warnings # pragma: no cover
from pandas._testing import assert_series_equal # pragma: no cover
from pandas.errors import PerformanceWarning # pragma: no cover

Series = pd.Series # pragma: no cover
tm = type('Mock', (object,), { 'maybe_produces_warning': lambda *args, **kwargs: warnings.catch_warnings(), 'assert_series_equal': assert_series_equal }) # pragma: no cover

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
