# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
# shifter index
s = [f"x{x:d}" for x in range(12)]

frame_xp = (
    frame.reindex(list(frame.index) + s)
    .rolling(window=25)
    .quantile(q)
    .shift(-12)
    .reindex(frame.index)
)
frame_rs = frame.rolling(window=25, center=True).quantile(q)
tm.assert_frame_equal(frame_xp, frame_rs)
