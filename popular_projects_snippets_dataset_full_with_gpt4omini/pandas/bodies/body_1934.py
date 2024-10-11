# Extracted from ./data/repos/pandas/pandas/tests/resample/test_timedelta.py
# GH 13223
index = pd.to_timedelta(["0s", pd.NaT, "2s"])
result = DataFrame({"value": [2, 3, 5]}, index).resample("1s").mean()
expected = DataFrame(
    {"value": [2.5, np.nan, 5.0]},
    index=timedelta_range("0 day", periods=3, freq="1S"),
)
tm.assert_frame_equal(result, expected)
