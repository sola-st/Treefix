# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_equals.py
# https://github.com/pandas-dev/pandas/issues/16603
a = CategoricalIndex(["A"], categories=["A", "B"])
b = CategoricalIndex(["A"], categories=["B", "A"])
c = CategoricalIndex(["C"], categories=["B", "A"])
assert a.equals(b)
assert not a.equals(c)
assert not b.equals(c)
