# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# invalid ufunc
s = Series(Categorical([1, 2, 3, 4]))
msg = "Object with dtype category cannot perform the numpy op log"
with pytest.raises(TypeError, match=msg):
    np.log(s)
