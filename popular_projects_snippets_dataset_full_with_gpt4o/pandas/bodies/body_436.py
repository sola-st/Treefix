# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_complex_dtype(int)
assert not com.is_complex_dtype(str)
assert not com.is_complex_dtype(pd.Series([1, 2]))
assert not com.is_complex_dtype(np.array(["a", "b"]))

assert com.is_complex_dtype(np.complex_)
assert com.is_complex_dtype(complex)
assert com.is_complex_dtype(np.array([1 + 1j, 5]))
