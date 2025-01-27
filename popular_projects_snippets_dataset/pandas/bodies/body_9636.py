# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
arr = np.array([1, 2, 3], dtype="int64")
arr = PandasArray(arr)
msg = "cannot perform not_a_method with type int"
with pytest.raises(TypeError, match=msg):
    arr._reduce(msg)
