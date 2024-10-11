# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_constructors.py
# GH#12288
orig = RangeIndex(10)
orig.name = "original"

copy = RangeIndex(orig)
copy.name = "copy"

assert orig.name == "original"
assert copy.name == "copy"

new = Index(copy)
assert new.name == "copy"

new.name = "new"
assert orig.name == "original"
assert copy.name == "copy"
assert new.name == "new"
