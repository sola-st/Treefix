# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
index = simple_index
i = Index(index.copy())
assert i.identical(index)

# we don't allow object dtype for RangeIndex
if isinstance(index, RangeIndex):
    exit()

same_values_different_type = Index(i, dtype=object)
assert not i.identical(same_values_different_type)

i = index.copy(dtype=object)
i = i.rename("foo")
same_values = Index(i, dtype=object)
assert same_values.identical(index.copy(dtype=object))

assert not i.identical(index)
assert Index(same_values, name="foo", dtype=object).identical(i)

assert not index.copy(dtype=object).identical(index.copy(dtype="int64"))
