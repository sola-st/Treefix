# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_subclass.py
sc = tm.SubclassedCategorical(["a", "b", "c"])
assert isinstance(sc, tm.SubclassedCategorical)
tm.assert_categorical_equal(sc, Categorical(["a", "b", "c"]))
