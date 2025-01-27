# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py

# names are assigned in setup
assert index_names == ["first", "second"]
level_names = [level.name for level in idx.levels]
assert level_names == index_names

# setting bad names on existing
index = idx
with pytest.raises(ValueError, match="^Length of names"):
    setattr(index, "names", list(index.names) + ["third"])
with pytest.raises(ValueError, match="^Length of names"):
    setattr(index, "names", [])

# initializing with bad names (should always be equivalent)
major_axis, minor_axis = idx.levels
major_codes, minor_codes = idx.codes
with pytest.raises(ValueError, match="^Length of names"):
    MultiIndex(
        levels=[major_axis, minor_axis],
        codes=[major_codes, minor_codes],
        names=["first"],
    )
with pytest.raises(ValueError, match="^Length of names"):
    MultiIndex(
        levels=[major_axis, minor_axis],
        codes=[major_codes, minor_codes],
        names=["first", "second", "third"],
    )

# names are assigned on index, but not transferred to the levels
index.names = ["a", "b"]
level_names = [level.name for level in index.levels]
assert level_names == ["a", "b"]
