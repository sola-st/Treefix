# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_astype.py
a = pd.array([0.1, 0.2, None], dtype="Float64")
expected = np.array(["0.1", "0.2", "<NA>"], dtype="U32")

tm.assert_numpy_array_equal(a.astype(str), expected)
tm.assert_numpy_array_equal(a.astype("str"), expected)
