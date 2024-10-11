# Extracted from ./data/repos/pandas/pandas/tests/frame/test_npfuncs.py
with np.errstate(all="ignore"):
    result = np.sqrt(float_frame)
assert isinstance(result, type(float_frame))
assert result.index is float_frame.index
assert result.columns is float_frame.columns

tm.assert_frame_equal(result, float_frame.apply(np.sqrt))
