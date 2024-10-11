# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
arr = SparseArray(arr_data).copy()

def setitem():
    arr[5] = 3

def setslice():
    arr[1:5] = 2

with pytest.raises(TypeError, match="assignment via setitem"):
    setitem()

with pytest.raises(TypeError, match="assignment via setitem"):
    setslice()
