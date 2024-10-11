# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
# test the string repr
index.name = "foo"
assert "'foo'" in str(index)
assert type(index).__name__ in str(index)
