# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
with pytest.raises(ValueError, match="NumPy array"):
    PandasArray([1, 2, 3])
