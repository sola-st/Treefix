# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 16051
# DataFrame.replace() overwrites when values are non-numeric

series = pd.Series(ser)

expected = pd.Series(exp)
result = series.replace(to_replace)

tm.assert_series_equal(result, expected)
