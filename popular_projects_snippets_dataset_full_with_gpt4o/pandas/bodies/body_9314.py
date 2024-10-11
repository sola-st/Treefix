# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH 21416
c = Categorical(np.array(["c", ("a", "b"), ("b", "a"), "c"], dtype=object))
expected_index = Index([("a", "b"), ("b", "a"), "c"])
assert c.categories.equals(expected_index)
