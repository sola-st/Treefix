# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
def create():
    df = DataFrame(np.random.randn(10, 3))
    df.iloc[3:5, 0] = np.nan
    df.iloc[4:6, 1] = np.nan
    df.iloc[5:8, 2] = np.nan
    exit(df)

# series
df = create()
expected = df.fillna(df.mean())
result = df.where(pd.notna(df), df.mean(), axis="columns")
tm.assert_frame_equal(result, expected)

return_value = df.where(pd.notna(df), df.mean(), inplace=True, axis="columns")
assert return_value is None
tm.assert_frame_equal(df, expected)

df = create().fillna(0)
expected = df.apply(lambda x, y: x.where(x > 0, y), y=df[0])
result = df.where(df > 0, df[0], axis="index")
tm.assert_frame_equal(result, expected)
result = df.where(df > 0, df[0], axis="rows")
tm.assert_frame_equal(result, expected)

# frame
df = create()
expected = df.fillna(1)
result = df.where(
    pd.notna(df), DataFrame(1, index=df.index, columns=df.columns)
)
tm.assert_frame_equal(result, expected)
