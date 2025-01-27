# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH #12169 : Resample category data with timedelta index
# construct Series from dict as data and TimedeltaIndex as index
# will result NaN in result Series data
expected = Series(
    data=["A", "B", "C"], index=pd.to_timedelta([0, 10, 20], unit="s")
)

result = Series(
    data={
        pd.to_timedelta(0, unit="s"): "A",
        pd.to_timedelta(10, unit="s"): "B",
        pd.to_timedelta(20, unit="s"): "C",
    },
    index=pd.to_timedelta([0, 10, 20], unit="s"),
)
tm.assert_series_equal(result, expected)
