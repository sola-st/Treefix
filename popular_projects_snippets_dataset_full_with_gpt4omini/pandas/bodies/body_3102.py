# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
df = DataFrame({"high": [True, False], "low": [False, False]})
rs = df.shift(1)
xp = DataFrame(
    np.array([[np.nan, np.nan], [True, False]], dtype=object),
    columns=["high", "low"],
)
tm.assert_frame_equal(rs, xp)
