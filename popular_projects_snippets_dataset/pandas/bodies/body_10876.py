# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
df = DataFrame({"A": list("aaaba")})
s = Series(list("aaaba"))

tm.assert_series_equal(df.groupby(s).ngroup(), s.groupby(s).ngroup())
