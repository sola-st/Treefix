# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
# https://github.com/pandas-dev/pandas/issues/33820
df = pd.DataFrame(data)
result = df.to_numpy(dtype=float, na_value=np.nan)
tm.assert_numpy_array_equal(result, expected)
