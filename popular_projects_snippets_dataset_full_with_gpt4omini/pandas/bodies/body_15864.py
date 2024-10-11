# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 24971, GH#23305
ser = pd.Series(categorical)
result = ser.replace({"A": 1, "B": 2})
expected = pd.Series(numeric).astype("category")
if 2 not in expected.cat.categories:
    # i.e. categories should be [1, 2] even if there are no "B"s present
    # GH#44940
    expected = expected.cat.add_categories(2)
tm.assert_series_equal(expected, result)
