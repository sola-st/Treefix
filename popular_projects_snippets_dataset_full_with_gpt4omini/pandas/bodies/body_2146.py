# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 14156 & GH 20445: argument will incur floating point errors
# but no premature rounding
result = to_datetime(1434743731.8770001, unit="s", cache=cache)
expected = Timestamp("2015-06-19 19:55:31.877000192")
assert result == expected
