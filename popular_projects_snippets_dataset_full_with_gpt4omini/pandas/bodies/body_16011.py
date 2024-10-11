# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# GH#19356 GH#21804
ser = Series(values)
result = ser.isin([-9, -0.5])
expected = Series([True, False])
tm.assert_series_equal(result, expected)
