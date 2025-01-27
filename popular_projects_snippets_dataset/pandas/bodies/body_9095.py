# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
# GH-34352
result = str(SparseDtype("int64", fill_value=0))
expected = "Sparse[int64, 0]"
assert result == expected

result = str(SparseDtype(object, fill_value="0"))
expected = "Sparse[object, '0']"
assert result == expected
