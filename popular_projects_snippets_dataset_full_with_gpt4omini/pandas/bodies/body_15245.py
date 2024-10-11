# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_xs.py
# GH#6258
dt = list(date_range("20130903", periods=3))
idx = MultiIndex.from_product([list("AB"), dt])
ser = Series([1, 3, 4, 1, 3, 4], index=idx)
expected = Series([1, 1], index=list("AB"))

result = ser.xs("20130903", level=1)
tm.assert_series_equal(result, expected)
