# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#12290
s1 = Series([Timestamp("2016-02-10", tz="America/Sao_Paulo")])
s2 = Series([Timestamp("2016-02-08", tz="America/Sao_Paulo")])
result = s1 - s2
expected = Series([Timedelta("2days")])
tm.assert_series_equal(result, expected)
result = s2 - s1
expected = Series([Timedelta("-2days")])
tm.assert_series_equal(result, expected)
