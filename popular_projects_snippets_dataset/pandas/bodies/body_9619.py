# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_to_numpy.py
con = pd.Series if box else pd.array
arr = con([0.0, 1.0, None], dtype="Float64")

result = arr.to_numpy(dtype="str")
expected = np.array([0.0, 1.0, pd.NA], dtype=f"{tm.ENDIAN}U32")
tm.assert_numpy_array_equal(result, expected)
