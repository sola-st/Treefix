# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
#   - assign multiple rows (mixed values) -> exp_multi_row
df = orig.copy()

key = slice(2, 4)
if indexer is tm.loc:
    key = slice("j", "k")

indexer(df)[key, :] = [["b", 2], ["b", 2]]
tm.assert_frame_equal(df, exp_multi_row)

df = orig.copy()
with pytest.raises(TypeError, match=msg1):
    indexer(df)[key, :] = [["c", 2], ["c", 2]]
