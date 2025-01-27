# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index = simple_index

idx = Index(index.copy())
assert idx.identical(index)

same_values_different_type = Index(idx, dtype=object)
assert not idx.identical(same_values_different_type)

idx = index.astype(dtype=object)
idx = idx.rename("foo")
same_values = Index(idx, dtype=object)
assert same_values.identical(idx)

assert not idx.identical(index)
assert Index(same_values, name="foo", dtype=object).identical(idx)

assert not index.astype(dtype=object).identical(index.astype(dtype=dtype))
