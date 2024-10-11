# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_analytics.py
with pytest.raises(NotImplementedError, match="to_frame"):
    idx.infer_objects()
