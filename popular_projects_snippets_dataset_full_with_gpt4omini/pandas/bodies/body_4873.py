# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
from l3.Runtime import _l_
values = Series(
    ["om", None, "foo_nom", "nom", "bar_foo", None, "foo", "regex", "rege."],
    dtype=nullable_string_dtype,
)
_l_(10224)
result = values.str.startswith("foo", na=na)
_l_(10225)
exp = Series(
    [False, na, True, False, False, na, True, False, False], dtype="boolean"
)
_l_(10226)
tm.assert_series_equal(result, exp)
_l_(10227)

result = values.str.startswith("rege.", na=na)
_l_(10228)
exp = Series(
    [False, na, False, False, False, na, False, False, True], dtype="boolean"
)
_l_(10229)
tm.assert_series_equal(result, exp)
_l_(10230)
