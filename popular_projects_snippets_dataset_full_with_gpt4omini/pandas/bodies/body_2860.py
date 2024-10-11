# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
datetime_frame.loc[datetime_frame.index[:5], "A"] = np.nan
datetime_frame.loc[datetime_frame.index[-5:], "A"] = np.nan

tm.assert_frame_equal(
    datetime_frame.ffill(), datetime_frame.fillna(method="ffill")
)
