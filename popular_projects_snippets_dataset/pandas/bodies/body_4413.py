# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# PeriodIndex
a = pd.PeriodIndex(["2012-01", "NaT", "2012-04"], freq="M")
b = pd.PeriodIndex(["2012-02-01", "2012-03-01", "NaT"], freq="D")
df = DataFrame({"a": a, "b": b})
assert df["a"].dtype == a.dtype
assert df["b"].dtype == b.dtype

# list of periods
df = DataFrame({"a": a.astype(object).tolist(), "b": b.astype(object).tolist()})
assert df["a"].dtype == a.dtype
assert df["b"].dtype == b.dtype
