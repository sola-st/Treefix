# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# MultiIndex tested separately
index = index_flat
new_name = "This is the new name for this index"

original_name = index.name
new_ind = index.set_names([new_name])
assert new_ind.name == new_name
assert index.name == original_name
res = index.rename(new_name, inplace=True)

# should return None
assert res is None
assert index.name == new_name
assert index.names == [new_name]
# FIXME: dont leave commented-out
# with pytest.raises(TypeError, match="list-like"):
#    # should still fail even if it would be the right length
#    ind.set_names("a")
with pytest.raises(ValueError, match="Level must be None"):
    index.set_names("a", level=0)

# rename in place just leaves tuples and other containers alone
name = ("A", "B")
index.rename(name, inplace=True)
assert index.name == name
assert index.names == [name]
