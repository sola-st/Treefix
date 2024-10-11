# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
msg = "Array with ndim > 2 are not supported"

with pytest.raises(TypeError, match=msg):
    algos.rank(arr)
