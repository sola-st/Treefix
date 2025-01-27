# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py

# dtypes
tsframe = datetime_frame.copy().astype(np.float32)
tsframe.loc[tsframe.index[:5], "A"] = np.nan
tsframe.loc[tsframe.index[-5:], "A"] = np.nan

zero_filled = tsframe.replace(np.nan, -1e8)
tm.assert_frame_equal(zero_filled, tsframe.fillna(-1e8))
tm.assert_frame_equal(zero_filled.replace(-1e8, np.nan), tsframe)

tsframe.loc[tsframe.index[:5], "A"] = np.nan
tsframe.loc[tsframe.index[-5:], "A"] = np.nan
tsframe.loc[tsframe.index[:5], "B"] = -1e8

b = tsframe["B"]
b[b == -1e8] = np.nan
tsframe["B"] = b
result = tsframe.fillna(method="bfill")
tm.assert_frame_equal(result, tsframe.fillna(method="bfill"))
