# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
from l3.Runtime import _l_
ser = Series(
    ["fooBAD__barBAD", "BAD_BADleroybrown", np.nan, "foo"], dtype=any_string_dtype
)
_l_(21000)
result = ser.str.fullmatch(".*BAD[_]+.*BAD", na=False)
_l_(21001)
expected_dtype = np.bool_ if any_string_dtype == "object" else "boolean"
_l_(21002)
expected = Series([True, False, False, False], dtype=expected_dtype)
_l_(21003)
tm.assert_series_equal(result, expected)
_l_(21004)
