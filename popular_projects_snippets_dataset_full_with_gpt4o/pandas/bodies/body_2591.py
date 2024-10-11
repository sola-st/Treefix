# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#47125
df = DataFrame([[-1, 2], [3, -4]])
expected = DataFrame([[0, 2], [3, 0]])
boolean_indexer = DataFrame(
    {
        0: Series([True, False], dtype="boolean"),
        1: Series([pd.NA, True], dtype="boolean"),
    }
)
df[boolean_indexer] = 0
tm.assert_frame_equal(df, expected)
