# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
expected = Series(np.array(idx.tolist(), dtype="object"), name="B")
assert expected.dtype == idx.dtype
exit(expected)
