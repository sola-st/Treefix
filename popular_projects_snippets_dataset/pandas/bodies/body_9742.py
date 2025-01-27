# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
# GH-19248, GH-32385
index = [
    Timestamp("20190101 09:00:30"),
    Timestamp("20190101 09:00:27"),
    Timestamp("20190101 09:00:20"),
    Timestamp("20190101 09:00:18"),
    Timestamp("20190101 09:00:10"),
]

df = DataFrame({"column": [3, 4, 4, 5, 6]}, index=index)
result = df.rolling("5s").min()
expected = DataFrame({"column": [3.0, 3.0, 4.0, 4.0, 6.0]}, index=index)
tm.assert_frame_equal(result, expected)
