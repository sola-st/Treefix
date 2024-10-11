# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
if cast_index:
    index = Index(vals, dtype=bool)
else:
    index = Index(vals)

assert type(index) is Index
assert index.dtype == bool
