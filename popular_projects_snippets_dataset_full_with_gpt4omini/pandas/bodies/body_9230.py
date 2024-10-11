# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# numpy ops
s = Series(Categorical([1, 2, 3, 4]))
with pytest.raises(TypeError, match="does not support reduction 'sum'"):
    np.sum(s)
