# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
# https://github.com/pandas-dev/pandas/issues/33820
df = pd.DataFrame(data)
result = df.to_numpy(dtype=dtype, na_value=na_value)
expected = np.array([[1, 1], [2, 2], [3, na_value]], dtype=dtype)
tm.assert_numpy_array_equal(result, expected)
