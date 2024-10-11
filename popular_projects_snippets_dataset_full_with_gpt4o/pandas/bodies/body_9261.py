# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# ndim > 1
msg = "> 1 ndim Categorical are not supported at this time"
with pytest.raises(NotImplementedError, match=msg):
    Categorical(np.array([list("abcd")]))
