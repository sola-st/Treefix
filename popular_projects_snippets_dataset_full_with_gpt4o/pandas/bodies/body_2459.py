# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#48016
df = DataFrame({"a": [1, 2, 3]}, dtype="Int64")
df.iloc[:, func([0])] = 5
expected = DataFrame({"a": [5, 5, 5]}, dtype="Int64")
tm.assert_frame_equal(df, expected)
