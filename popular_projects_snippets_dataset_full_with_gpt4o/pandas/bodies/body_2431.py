# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#3216 ndarray
f = float_string_frame.copy()
piece = float_string_frame.loc[f.index[:2], ["A", "B"]]
key = (f.index[slice(-2, None)], ["A", "B"])
f.loc[key] = piece.values
tm.assert_almost_equal(f.loc[f.index[-2:], ["A", "B"]].values, piece.values)
