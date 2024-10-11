# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isetitem.py
# GH#49922
df = DataFrame([[1, 2, 3], [4, 5, 6]])
rhs = DataFrame([[11], [13]], dtype="Int64")

df.isetitem(2, rhs)
expected = DataFrame(
    {
        0: [1, 4],
        1: [2, 5],
        2: Series([11, 13], dtype="Int64"),
    }
)
tm.assert_frame_equal(df, expected)
