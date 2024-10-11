# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex_like.py
other = float_frame.reindex(index=float_frame.index[:10], columns=["C", "B"])

tm.assert_frame_equal(other, float_frame.reindex_like(other))
