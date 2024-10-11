# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# GH#5021

expected = Series([True, True, False, False, False])
expected2 = Series([False, True, False, False, False])

# datetime64[ns]
s = Series(date_range("jan-01-2013", "jan-05-2013"))

result = s.isin(s[0:2])
tm.assert_series_equal(result, expected)

result = s.isin(s[0:2].values)
tm.assert_series_equal(result, expected)

result = s.isin([s[1]])
tm.assert_series_equal(result, expected2)

result = s.isin([np.datetime64(s[1])])
tm.assert_series_equal(result, expected2)

result = s.isin(set(s[0:2]))
tm.assert_series_equal(result, expected)

# timedelta64[ns]
s = Series(pd.to_timedelta(range(5), unit="d"))
result = s.isin(s[0:2])
tm.assert_series_equal(result, expected)
