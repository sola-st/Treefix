# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
idx1 = TimedeltaIndex(
    [
        "1 day",
        NaT,
        "1 day 00:00:01",
        NaT,
        "1 day 00:00:01",
        "5 day 00:00:03",
    ]
)
# Check pd.NaT is handles as the same as np.nan
result = idx1 < idx2
expected = np.array([True, False, False, False, True, False])
tm.assert_numpy_array_equal(result, expected)

result = idx2 > idx1
expected = np.array([True, False, False, False, True, False])
tm.assert_numpy_array_equal(result, expected)

result = idx1 <= idx2
expected = np.array([True, False, False, False, True, True])
tm.assert_numpy_array_equal(result, expected)

result = idx2 >= idx1
expected = np.array([True, False, False, False, True, True])
tm.assert_numpy_array_equal(result, expected)

result = idx1 == idx2
expected = np.array([False, False, False, False, False, True])
tm.assert_numpy_array_equal(result, expected)

result = idx1 != idx2
expected = np.array([True, True, True, True, True, False])
tm.assert_numpy_array_equal(result, expected)
