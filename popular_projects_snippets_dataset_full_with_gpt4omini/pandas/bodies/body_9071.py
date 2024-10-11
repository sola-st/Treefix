# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
with pytest.raises(TypeError, match="expected dimension <= 1 data"):
    SparseArray(np.arange(10).reshape((2, 5)))
