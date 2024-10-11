# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
arr = PandasArray(np.array([1, 2, 3]))
msg = "the 'keepdims' parameter is not supported .*all"
with pytest.raises(ValueError, match=msg):
    arr.all(keepdims=True)
