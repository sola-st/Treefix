# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#31644
ser = pd.Series(["A", "B"], dtype="string")
res = ser.replace(r".", "C", regex=True)
expected = pd.Series(["C", "C"], dtype="string")
tm.assert_series_equal(res, expected)
