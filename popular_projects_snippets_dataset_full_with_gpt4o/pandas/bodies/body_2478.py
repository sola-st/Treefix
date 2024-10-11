# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# mask with single True
df = orig.copy()

mask = df.index == "j"
key = 0
if indexer is tm.loc:
    key = df.columns[key]

indexer(df)[mask, key] = "b"
tm.assert_frame_equal(df, exp_single_cats_value)
