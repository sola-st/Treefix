# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py
# alignment raises unless we transpose
op = comparison_op
cat = Categorical(["a", "b", 2, "a"])
df = DataFrame(cat)
msg = "Unable to coerce to Series, length must be 1: given 4"
with pytest.raises(ValueError, match=msg):
    op(cat, df)
