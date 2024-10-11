# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
other = np.arange(10).astype(dtype)
result = op(NaT, other)

expected = np.empty(other.shape, dtype=out_dtype)
expected.fill("NaT")
tm.assert_numpy_array_equal(result, expected)
