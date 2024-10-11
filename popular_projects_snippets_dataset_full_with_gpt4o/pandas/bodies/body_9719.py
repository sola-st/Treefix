# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = DataFrame(
    {"B": range(5), "C": date_range("20130101 09:00:00", periods=5, freq="3s")}
)

df["A"] = [
    Timestamp("20130101 09:00:00"),
    Timestamp("20130101 09:00:02"),
    Timestamp("20130101 09:00:03"),
    Timestamp("20130101 09:00:05"),
    Timestamp("20130101 09:00:06"),
]

# we are doing simulating using 'on'
expected = df.set_index("A").rolling("2s").B.sum().reset_index(drop=True)

result = df.rolling("2s", on="A").B.sum()
tm.assert_series_equal(result, expected)

# test as a frame
# we should be ignoring the 'on' as an aggregation column
# note that the expected is setting, computing, and resetting
# so the columns need to be switched compared
# to the actual result where they are ordered as in the
# original
expected = (
    df.set_index("A").rolling("2s")[["B"]].sum().reset_index()[["B", "A"]]
)

result = df.rolling("2s", on="A")[["B"]].sum()
tm.assert_frame_equal(result, expected)
