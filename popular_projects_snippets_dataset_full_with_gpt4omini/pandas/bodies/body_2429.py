# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#3216 rows unaligned
f = float_string_frame.copy()
piece = DataFrame(
    [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0]],
    index=list(f.index[0:2]) + ["foo", "bar"],
    columns=["A", "B"],
)
key = (f.index[slice(None, 2)], ["A", "B"])
f.loc[key] = piece
tm.assert_almost_equal(
    f.loc[f.index[0:2:], ["A", "B"]].values, piece.values[0:2]
)
