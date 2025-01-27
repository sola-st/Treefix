# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
# GH#17574
data = [False, 0, 100.0, 0.0]
arr = SparseArray(data, dtype=object, fill_value=False)
assert arr.dtype == SparseDtype(object, False)
assert arr.fill_value is False
arr_expected = np.array(data, dtype=object)
it = (type(x) == type(y) and x == y for x, y in zip(arr, arr_expected))
assert np.fromiter(it, dtype=np.bool_).all()
