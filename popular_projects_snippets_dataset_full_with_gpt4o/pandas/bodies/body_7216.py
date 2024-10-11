# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index([0, 1, 2])
assert index.get_loc(1) == 1
