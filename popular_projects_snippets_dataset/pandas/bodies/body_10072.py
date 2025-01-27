# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
"""Replicate result expected in GH #6297"""
indices = [datetime(1975, 1, i) for i in range(1, 6)]
# So that we can have 2 datapoints on one of the days
indices.append(datetime(1975, 1, 3, 6, 0))
series = Series(range(1, 7), index=indices)
# Use floats instead of ints as values
series = series.map(lambda x: float(x))
# Sort chronologically
series = series.sort_index()

expected = Series(
    [1.0, 2.0, 6.0, 4.0, 5.0],
    index=DatetimeIndex([datetime(1975, 1, i, 0) for i in range(1, 6)], freq="D"),
)[::step]
x = series.resample("D").max().rolling(window=1, step=step).max()
tm.assert_series_equal(expected, x)
