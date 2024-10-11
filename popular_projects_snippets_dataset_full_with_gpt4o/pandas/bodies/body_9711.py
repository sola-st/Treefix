# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = DataFrame(
    {"B": [0, 1, 2, np.nan, 4]},
    index=[
        Timestamp("20130101 09:00:00"),
        Timestamp("20130101 09:00:02"),
        Timestamp("20130101 09:00:03"),
        Timestamp("20130101 09:00:05"),
        Timestamp("20130101 09:00:06"),
    ],
)
df
df.rolling("2s").sum()
