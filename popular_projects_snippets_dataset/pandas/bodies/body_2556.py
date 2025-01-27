# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#47425
df = DataFrame({"a": [1, 2]})
df["a"] = Series([1, 2], dtype="Int64")
expected = DataFrame({"a": [1, 2]}, dtype="Int64")
tm.assert_frame_equal(df, expected)
