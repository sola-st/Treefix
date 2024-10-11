# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#46896
df = DataFrame(columns=["a", "b"], data=[[1, 2], [3, 4]])
df["c"] = DataFrame({"a": [10, 11]}, dtype=any_numeric_ea_dtype)
expected = DataFrame(
    {
        "a": [1, 3],
        "b": [2, 4],
        "c": Series([10, 11], dtype=any_numeric_ea_dtype),
    }
)
tm.assert_frame_equal(df, expected)
