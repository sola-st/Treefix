# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
arr = SparseArray([0, 1])
ser = pd.Series(arr)

result = getattr(ser.sparse, attr)
expected = getattr(arr, attr)
assert result == expected
