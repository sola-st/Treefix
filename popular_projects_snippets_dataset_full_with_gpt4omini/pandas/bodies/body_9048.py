# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
a = pd.array([0, 0], dtype=SparseDtype("int64"))
result = a.take([0, 1], allow_fill=True, fill_value=np.nan)
tm.assert_sp_array_equal(a, result)
