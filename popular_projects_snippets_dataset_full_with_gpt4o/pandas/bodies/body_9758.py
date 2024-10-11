# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py
# shifter index
s = [f"x{x:d}" for x in range(12)]

frame_xp = (
    getattr(
        frame.reindex(list(frame.index) + s).rolling(window=25),
        roll_func,
    )()
    .shift(-12)
    .reindex(frame.index)
)
frame_rs = getattr(frame.rolling(window=25, center=True), roll_func)()
tm.assert_frame_equal(frame_xp, frame_rs)
