# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
dates = date_range("01-Jan-2013", "01-Jan-2014", freq="MS")[0:-1]
s1 = Series(np.random.randn(len(dates)), index=dates, name="value")
s2 = Series(np.random.randn(len(dates)), index=dates, name="value")

result = concat([s1, s2], axis=1, ignore_index=True)
expected = Index(range(2))

tm.assert_index_equal(result.columns, expected, exact=True)
