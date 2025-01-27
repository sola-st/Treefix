# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
datetime_frame.loc[datetime_frame.index[:5], "A"] = np.nan
datetime_frame.loc[datetime_frame.index[-5:], "A"] = np.nan

zero_filled = datetime_frame.replace(np.nan, -1e8)
tm.assert_frame_equal(zero_filled, datetime_frame.fillna(-1e8))
tm.assert_frame_equal(zero_filled.replace(-1e8, np.nan), datetime_frame)

datetime_frame.loc[datetime_frame.index[:5], "A"] = np.nan
datetime_frame.loc[datetime_frame.index[-5:], "A"] = np.nan
datetime_frame.loc[datetime_frame.index[:5], "B"] = -1e8

# empty
df = DataFrame(index=["a", "b"])
tm.assert_frame_equal(df, df.replace(5, 7))

# GH 11698
# test for mixed data types.
df = DataFrame(
    [("-", pd.to_datetime("20150101")), ("a", pd.to_datetime("20150102"))]
)
df1 = df.replace("-", np.nan)
expected_df = DataFrame(
    [(np.nan, pd.to_datetime("20150101")), ("a", pd.to_datetime("20150102"))]
)
tm.assert_frame_equal(df1, expected_df)
