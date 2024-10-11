# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#45469
df = DataFrame({"a": ["a", "b", "c"]}, dtype="string")
df.iloc[0, :] = val
expected = DataFrame({"a": [pd.NA, "b", "c"]}, dtype="string")
tm.assert_frame_equal(df, expected)
