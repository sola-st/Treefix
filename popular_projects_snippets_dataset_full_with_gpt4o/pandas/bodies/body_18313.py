# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
rng = timedelta_range("1 days", periods=10)

result = rng < rng[3]
expected = np.array([True, True, True] + [False] * 7)
tm.assert_numpy_array_equal(result, expected)

result = rng == list(rng)
exp = rng == rng
tm.assert_numpy_array_equal(result, exp)
