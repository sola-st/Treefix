# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
arr = np.array(
    [
        NaT,
        np.datetime64("NaT"),
        np.timedelta64("NaT"),
        np.datetime64("NaT", "s"),
    ]
)
result = isna(arr)
expected = np.array([True] * 4)
tm.assert_numpy_array_equal(result, expected)
