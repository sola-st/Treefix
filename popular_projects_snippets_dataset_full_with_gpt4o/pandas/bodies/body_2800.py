# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH#38566
obj = frame_or_series(
    [0, 1, 2, 3],
    index=date_range("2020-01-01 00:00:00", periods=4, freq="H", tz="UTC"),
)
new_index = date_range("2020-01-01 00:01:00", periods=4, freq="H", tz="UTC")
result = obj.reindex(new_index, method=method, tolerance=pd.Timedelta("1 hour"))
expected = frame_or_series(exp_values, index=new_index)
tm.assert_equal(result, expected)
