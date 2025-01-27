# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
a = pd.array([1, 2, None], dtype="Int64")
expected = np.array(["1", "2", "<NA>"], dtype=f"{tm.ENDIAN}U21")

tm.assert_numpy_array_equal(a.astype(str), expected)
tm.assert_numpy_array_equal(a.astype("str"), expected)
