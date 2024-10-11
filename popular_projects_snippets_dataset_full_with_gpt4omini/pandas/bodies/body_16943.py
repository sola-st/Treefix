# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH 3232
# Monotonic index result
dr = date_range("01-Jan-2013", periods=100, freq="50L", tz="UTC")
data = list(range(100))
expected = DataFrame(data, index=dr)
result = concat([expected[:50], expected[50:]])
tm.assert_frame_equal(result, expected)

# Non-monotonic index result
result = concat([expected[50:], expected[:50]])
expected = DataFrame(data[50:] + data[:50], index=dr[50:].append(dr[:50]))
expected.index._data.freq = None
tm.assert_frame_equal(result, expected)
