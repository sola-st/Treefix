# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# GH#45206
arr = array([0], dtype=any_numeric_ea_dtype)

idx = Index(arr, dtype=object)
assert idx.dtype == object
