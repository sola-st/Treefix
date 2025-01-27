# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#41215, GH#44940
ser = pd.Series(["abc", "def"], dtype="string")
res = ser.replace(["abc", "any other string"], "xyz")
expected = pd.Series(["xyz", "def"], dtype="string")
tm.assert_series_equal(res, expected)
