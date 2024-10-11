# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
# GH-32385
df = DataFrame({"column": []}, index=[])
result = df.rolling("5s").min()
expected = DataFrame({"column": []}, index=[])
tm.assert_frame_equal(result, expected)
