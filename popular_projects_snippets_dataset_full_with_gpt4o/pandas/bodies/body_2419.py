# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
f = float_frame
ix = f.loc

expected = f.reindex(columns=["B", "D"])
result = ix[:, [False, True, False, True]]
tm.assert_frame_equal(result, expected)

expected = f.reindex(index=f.index[5:10], columns=["B", "D"])
result = ix[f.index[5:10], [False, True, False, True]]
tm.assert_frame_equal(result, expected)

boolvec = f.index > f.index[7]
expected = f.reindex(index=f.index[boolvec])
result = ix[boolvec]
tm.assert_frame_equal(result, expected)
result = ix[boolvec, :]
tm.assert_frame_equal(result, expected)

result = ix[boolvec, f.columns[2:]]
expected = f.reindex(index=f.index[boolvec], columns=["C", "D"])
tm.assert_frame_equal(result, expected)
