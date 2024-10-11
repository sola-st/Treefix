# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#3216 key is unaligned with values
f = float_string_frame.copy()
piece = f.loc[f.index[:2], ["A"]]
piece.index = f.index[-2:]
key = (f.index[slice(-2, None)], ["A", "B"])
f.loc[key] = piece
piece["B"] = np.nan
tm.assert_almost_equal(f.loc[f.index[-2:], ["A", "B"]].values, piece.values)
