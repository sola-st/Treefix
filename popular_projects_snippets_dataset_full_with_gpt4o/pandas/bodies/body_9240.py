# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
cat = Categorical(["a", "b", "c", "d", "a", "b", "c"])
sliced = cat[3]
assert sliced == "d"

sliced = cat[3:5]
expected = Categorical(["d", "a"], categories=["a", "b", "c", "d"])
tm.assert_categorical_equal(sliced, expected)
