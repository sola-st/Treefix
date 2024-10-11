# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# boolean indexing
# GH#4879
df = DataFrame(
    np.arange(12).reshape(3, 4), columns=["A", "B", "C", "D"], dtype="float64"
)
expected = df[df.C > 6]
expected.columns = df_dup_cols.columns

df = df_dup_cols
result = df[df.C > 6]

tm.assert_frame_equal(result, expected)
result.dtypes
str(result)
