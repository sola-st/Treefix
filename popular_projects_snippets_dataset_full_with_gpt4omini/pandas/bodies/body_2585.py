# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#37550
# Dtype is only changed when value to set is a Series and indexer is
# empty/bool all False
df = DataFrame({"a": ["a"], "b": [1], "c": [1]})
indexer = box([False])
df.loc[indexer, ["b"]] = 10 - df["c"]
expected = DataFrame({"a": ["a"], "b": [1], "c": [1]})
tm.assert_frame_equal(df, expected)

df.loc[indexer, ["b"]] = 9
tm.assert_frame_equal(df, expected)
