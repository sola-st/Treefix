# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
# GH#11856
arr = SparseArray(["A", "A", np.nan, "B"], dtype=object)
assert arr.dtype == SparseDtype(object)
assert np.isnan(arr.fill_value)

arr = SparseArray(["A", "A", np.nan, "B"], dtype=object, fill_value="A")
assert arr.dtype == SparseDtype(object, "A")
assert arr.fill_value == "A"
