# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_value_counts.py
# GH32146
out = ser.value_counts(dropna=dropna)
tm.assert_series_equal(out, exp)
