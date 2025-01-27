# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH 3216

# already aligned
f = float_string_frame.copy()
piece = DataFrame(
    [[1.0, 2.0], [3.0, 4.0]], index=f.index[0:2], columns=["A", "B"]
)
key = (f.index[slice(None, 2)], ["A", "B"])
f.loc[key] = piece
tm.assert_almost_equal(f.loc[f.index[0:2], ["A", "B"]].values, piece.values)
