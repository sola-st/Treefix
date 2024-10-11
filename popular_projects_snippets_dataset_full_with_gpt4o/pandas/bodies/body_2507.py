# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py

# where
df = DataFrame(
    np.arange(12).reshape(3, 4), columns=["A", "B", "C", "D"], dtype="float64"
)
# `df > 6` is a DataFrame with the same shape+alignment as df
expected = df[df > 6]
expected.columns = df_dup_cols.columns

df = df_dup_cols
result = df[df > 6]

tm.assert_frame_equal(result, expected)
result.dtypes
str(result)
