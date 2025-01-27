# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 23803
strlen_frame = float_frame.applymap(lambda x: len(str(x)))
float_frame_with_na = float_frame.copy()
mask = np.random.randint(0, 2, size=float_frame.shape, dtype=bool)
float_frame_with_na[mask] = pd.NA
strlen_frame_na_ignore = float_frame_with_na.applymap(
    lambda x: len(str(x)), na_action="ignore"
)
strlen_frame_with_na = strlen_frame.copy()
strlen_frame_with_na[mask] = pd.NA
tm.assert_frame_equal(strlen_frame_na_ignore, strlen_frame_with_na)
