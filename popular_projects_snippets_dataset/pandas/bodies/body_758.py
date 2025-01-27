# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
result = isna([NaT])
exp = np.array([True])
tm.assert_numpy_array_equal(result, exp)

result = isna(np.array([NaT], dtype=object))
exp = np.array([True])
tm.assert_numpy_array_equal(result, exp)
