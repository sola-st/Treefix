# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
grouped = df.groupby("A")

aggfun_0 = lambda ser: ser.size
result = grouped.agg(aggfun_0)
foosum = (df.A == "foo").sum()
barsum = (df.A == "bar").sum()
K = len(result.columns)

# GH5782
exp = Series(np.array([foosum] * K), index=list("BCD"), name="foo")
tm.assert_series_equal(result.xs("foo"), exp)

exp = Series(np.array([barsum] * K), index=list("BCD"), name="bar")
tm.assert_almost_equal(result.xs("bar"), exp)

def aggfun_1(ser):
    exit(ser.size)

result = DataFrame().groupby(df.A).agg(aggfun_1)
assert isinstance(result, DataFrame)
assert len(result) == 0
