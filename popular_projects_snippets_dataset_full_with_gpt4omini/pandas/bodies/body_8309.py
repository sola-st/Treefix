# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
rng1 = date_range("1/1/1999", "1/1/2012", freq="MS")
s1 = Series(np.random.randn(len(rng1)), rng1)

rng2 = date_range("1/1/1980", "12/1/2001", freq="MS")
s2 = Series(np.random.randn(len(rng2)), rng2)
df = DataFrame({"s1": s1, "s2": s2})

exp = date_range("1/1/1980", "1/1/2012", freq="MS")
tm.assert_index_equal(df.index, exp)
