# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 6273
# create from a series, passing a freq
dts = ["1-1-1990", "2-1-1990", "3-1-1990", "4-1-1990", "5-1-1990"]
expected = DatetimeIndex(dts, freq="MS")

df = DataFrame(np.random.rand(5, 3))
df["date"] = dts
result = DatetimeIndex(df["date"], freq="MS")

assert df["date"].dtype == object
expected.name = "date"
tm.assert_index_equal(result, expected)

expected = Series(dts, name="date")
tm.assert_series_equal(df["date"], expected)

# GH 6274
# infer freq of same
freq = pd.infer_freq(df["date"])
assert freq == "MS"
