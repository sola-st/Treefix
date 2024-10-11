import pandas as pd # pragma: no cover
from pandas.api.types import CategoricalDtype # pragma: no cover
import numpy as np # pragma: no cover

Series = pd.Series # pragma: no cover
na = pd.NA # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': pd.testing.assert_series_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
from l3.Runtime import _l_
values = Series(
    ["om", None, "foo_nom", "nom", "bar_foo", None, "foo", "regex", "rege."],
    dtype=nullable_string_dtype,
)
_l_(21274)
result = values.str.startswith("foo", na=na)
_l_(21275)
exp = Series(
    [False, na, True, False, False, na, True, False, False], dtype="boolean"
)
_l_(21276)
tm.assert_series_equal(result, exp)
_l_(21277)

result = values.str.startswith("rege.", na=na)
_l_(21278)
exp = Series(
    [False, na, False, False, False, na, False, False, True], dtype="boolean"
)
_l_(21279)
tm.assert_series_equal(result, exp)
_l_(21280)
