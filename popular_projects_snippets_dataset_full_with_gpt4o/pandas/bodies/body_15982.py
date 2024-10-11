# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
# index with name
renamer = Series(
    np.arange(4), index=Index(["a", "b", "c", "d"], name="name"), dtype="int64"
)
renamed = renamer.rename({})
assert renamed.index.name == renamer.index.name
