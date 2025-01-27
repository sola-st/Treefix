# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH17884
expected = Categorical(["a", "b"], categories=["a", "b", "c"])

result = Categorical.from_codes([0, 1], categories=klass(["a", "b", "c"]))
tm.assert_categorical_equal(result, expected)
