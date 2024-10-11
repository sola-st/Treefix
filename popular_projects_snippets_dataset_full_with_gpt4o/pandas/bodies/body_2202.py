# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 12585
warning_msg = (
    "Parsing dates in .* format when dayfirst=.* was specified. "
    "Pass `dayfirst=.*` or specify a format to silence this warning."
)

# CASE 1: valid input
arr = ["31/12/2014", "10/03/2011"]
expected = DatetimeIndex(
    ["2014-12-31", "2011-03-10"], dtype="datetime64[ns]", freq=None
)

# A. dayfirst arg correct, no warning
res1 = to_datetime(arr, dayfirst=True)
tm.assert_index_equal(expected, res1)

# B. dayfirst arg incorrect, warning
with tm.assert_produces_warning(UserWarning, match=warning_msg):
    res2 = to_datetime(arr, dayfirst=False)
tm.assert_index_equal(expected, res2)
