# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
rng = timedelta_range("1 days", periods=5)._data
other = np.array([0, 1, 2, rng[3], Timestamp("2021-01-01")])

result = rng == other
expected = np.array([False, False, False, True, False])
tm.assert_numpy_array_equal(result, expected)

result = rng != other
tm.assert_numpy_array_equal(result, ~expected)

msg = "Invalid comparison between|Cannot compare type|not supported between"
with pytest.raises(TypeError, match=msg):
    rng < other
with pytest.raises(TypeError, match=msg):
    rng > other
with pytest.raises(TypeError, match=msg):
    rng <= other
with pytest.raises(TypeError, match=msg):
    rng >= other
