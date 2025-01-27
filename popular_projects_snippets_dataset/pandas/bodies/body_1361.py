# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#36741
df = DataFrame({"flag": ["x", "y", "z"], "value": [1, 3, 4]})
indexer = klass([True, False, False])
df.iloc[indexer, 1] = df.iloc[indexer, 1] * 2
expected = DataFrame({"flag": ["x", "y", "z"], "value": [2, 3, 4]})
tm.assert_frame_equal(df, expected)
