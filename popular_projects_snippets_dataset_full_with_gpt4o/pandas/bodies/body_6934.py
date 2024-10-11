# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_constructors.py
# see gh-10697: if we are constructing from a mixed list of tuples,
# make sure that we are independent of the sorting order.
index = Index(index_vals)
assert isinstance(index, Index)
assert not isinstance(index, MultiIndex)
