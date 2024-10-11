# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
c1 = Categorical([], categories=["a", "b"])
c2 = Categorical([], categories=["a"])

msg = "Categoricals can only be compared if 'categories' are the same."
with pytest.raises(TypeError, match=msg):
    c1 == c2
