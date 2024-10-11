# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_function.py
# No arguments
result = data.round()
expected = pd.array(
    np.round(data.to_numpy(dtype=numpy_dtype, na_value=None)), dtype=data.dtype
)
tm.assert_extension_array_equal(result, expected)

# Decimals argument
result = data.round(decimals=2)
expected = pd.array(
    np.round(data.to_numpy(dtype=numpy_dtype, na_value=None), decimals=2),
    dtype=data.dtype,
)
tm.assert_extension_array_equal(result, expected)
