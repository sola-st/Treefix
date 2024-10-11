# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
casted = DataFrame(float_frame._mgr, dtype=int)
expected = DataFrame(float_frame._series, dtype=int)
tm.assert_frame_equal(casted, expected)

casted = DataFrame(float_frame._mgr, dtype=np.int32)
expected = DataFrame(float_frame._series, dtype=np.int32)
tm.assert_frame_equal(casted, expected)
