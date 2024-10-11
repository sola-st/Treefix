# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_join.py
if idx.is_unique:
    joined = idx.join(idx, how=join_type)
    assert (idx == joined).all()
