# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
if cast_index:
    index = Index(vals, dtype=object)
    assert isinstance(index, Index)
    assert index.dtype == object
else:
    index = Index(vals)
    assert isinstance(index, DatetimeIndex)
