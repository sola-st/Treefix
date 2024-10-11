# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
# shifter index
s = [f"x{x:d}" for x in range(12)]
minp = 10

frame_xp = (
    frame.reindex(list(frame.index) + s)
    .rolling(window=25, min_periods=minp)
    .apply(f, raw=raw)
    .shift(-12)
    .reindex(frame.index)
)
frame_rs = frame.rolling(window=25, min_periods=minp, center=True).apply(f, raw=raw)
tm.assert_frame_equal(frame_xp, frame_rs)
