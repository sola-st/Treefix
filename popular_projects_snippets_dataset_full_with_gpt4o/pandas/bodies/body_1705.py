# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
# GH 9925
n = 20
data = np.random.randn(n, 4).astype("int64")
normal_df = DataFrame(data, columns=["A", "B", "C", "D"])
normal_df["key"] = [1, 2, np.nan, 4, 5] * 4

dt_df = DataFrame(data, columns=["A", "B", "C", "D"])
dt_df["key"] = [
    datetime(2013, 1, 1),
    datetime(2013, 1, 2),
    pd.NaT,
    datetime(2013, 1, 4),
    datetime(2013, 1, 5),
] * 4

normal_grouped = normal_df.groupby("key")
dt_grouped = dt_df.groupby(Grouper(key="key", freq="D"))

normal_result = normal_grouped.size()
dt_result = dt_grouped.size()

pad = Series([0], index=[3])
expected = pd.concat([normal_result, pad])
expected = expected.sort_index()
expected.index = date_range(
    start="2013-01-01", freq="D", periods=5, name="key"
)._with_freq(None)
tm.assert_series_equal(expected, dt_result)
assert dt_result.index.name == "key"
