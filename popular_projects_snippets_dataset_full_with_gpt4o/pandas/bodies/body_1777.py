# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# #1596
rng = date_range("2012-06-12", periods=4, freq="h").as_unit(unit)

ts = Series(np.random.randn(len(rng)), index=rng)

result = ts.resample("20min").aggregate(["mean", "sum"])
assert isinstance(result, DataFrame)
