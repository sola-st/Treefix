# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_analytics.py
# this blows up
with pytest.raises(IndexError, match="^Too many levels"):
    idx.reorder_levels([2, 1, 0])
