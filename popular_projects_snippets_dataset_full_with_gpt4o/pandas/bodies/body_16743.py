# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 23020
df = DataFrame({"A": Series([1, 2, np.nan], dtype="Int64"), "B": 1})
result = merge(df, df, on="A")
expected = DataFrame(
    {"A": Series([1, 2, np.nan], dtype="Int64"), "B_x": 1, "B_y": 1}
)
tm.assert_frame_equal(result, expected)
