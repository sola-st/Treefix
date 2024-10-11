# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
idx = simple_index
if idx.is_unique:
    joined = idx.join(idx, how=join_type)
    assert (idx == joined).all()
