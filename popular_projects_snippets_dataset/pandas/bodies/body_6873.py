# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
index = index_flat

for func in (copy, deepcopy):
    idx_copy = func(index)
    assert idx_copy is not index
    assert idx_copy.equals(index)

new_copy = index.copy(deep=True, name="banana")
assert new_copy.name == "banana"
