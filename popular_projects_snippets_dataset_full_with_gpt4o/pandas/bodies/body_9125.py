# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_subclass.py
sc = tm.SubclassedCategorical(["a", "b", "c"])
res = sc.map(lambda x: x.upper())
assert isinstance(res, tm.SubclassedCategorical)
exp = Categorical(["A", "B", "C"])
tm.assert_categorical_equal(res, exp)
