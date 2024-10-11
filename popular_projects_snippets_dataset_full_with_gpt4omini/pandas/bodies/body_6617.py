# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
i = RangeIndex(5, name="Foo")
i_copy = i.copy()
assert i_copy is not i
assert i_copy.identical(i)
assert i_copy._range == range(0, 5, 1)
assert i_copy.name == "Foo"
