# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
"""
    Check that we either have a RangeIndex or that this index *cannot*
    be represented as a RangeIndex.
    """
if not isinstance(index, RangeIndex) and len(index) > 0:
    diff = index[:-1] - index[1:]
    assert not (diff == diff[0]).all()
