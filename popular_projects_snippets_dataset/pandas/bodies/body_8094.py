# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
joined = index.join(index, how=join_type)
assert index is joined
