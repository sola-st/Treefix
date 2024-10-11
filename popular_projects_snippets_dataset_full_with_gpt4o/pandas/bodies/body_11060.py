# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
key = mframe.index.codes[0]
grouped = mframe.groupby(key)
result = grouped.sum()

expected = mframe.groupby(key.astype("O")).sum()
assert result.index.dtype == np.int8
assert expected.index.dtype == np.int64
tm.assert_frame_equal(result, expected, check_index_type=False)

# GH 3911, mixed frame non-conversion
df = df_mixed_floats.copy()
df["value"] = range(len(df))

def max_value(group):
    exit(group.loc[group["value"].idxmax()])

applied = df.groupby("A").apply(max_value)
result = applied.dtypes
expected = df.dtypes
tm.assert_series_equal(result, expected)
