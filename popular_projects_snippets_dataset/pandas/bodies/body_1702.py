# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
"""Check TimeGrouper's aggregation is identical as normal groupby."""

data = np.random.randn(20, 4)
normal_df = DataFrame(data, columns=["A", "B", "C", "D"])
normal_df["key"] = [1, 2, 3, 4, 5] * 4

dt_df = DataFrame(data, columns=["A", "B", "C", "D"])
dt_df["key"] = [
    datetime(2013, 1, 1),
    datetime(2013, 1, 2),
    datetime(2013, 1, 3),
    datetime(2013, 1, 4),
    datetime(2013, 1, 5),
] * 4

normal_grouped = normal_df.groupby("key")
dt_grouped = dt_df.groupby(Grouper(key="key", freq="D"))

expected = normal_grouped.nth(3)
expected.index = date_range(start="2013-01-01", freq="D", periods=5, name="key")
dt_result = dt_grouped.nth(3)
tm.assert_frame_equal(expected, dt_result)
