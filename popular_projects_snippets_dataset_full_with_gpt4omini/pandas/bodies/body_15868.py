# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 9113
# BUG: replace int64 dtype with bool coerces to int64

series = pd.Series(ser)
result = series.replace(2, True)
expected = pd.Series(exp)

tm.assert_series_equal(result, expected)
