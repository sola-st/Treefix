# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
# shifter index
s = [f"x{x:d}" for x in range(12)]

frame_xp = (
    getattr(
        frame.reindex(list(frame.index) + s).rolling(window=25, min_periods=minp),
        roll_func,
    )(**kwargs)
    .shift(-12)
    .reindex(frame.index)
)
frame_rs = getattr(
    frame.rolling(window=25, min_periods=minp, center=True), roll_func
)(**kwargs)
if fill_value is not None:
    frame_xp = frame_xp.fillna(fill_value)
tm.assert_frame_equal(frame_xp, frame_rs)
