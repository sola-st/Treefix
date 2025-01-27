# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
gp = nulls_df.groupby(["A", "B"], dropna=group_dropna)
result = gp.value_counts(normalize=True, sort=True, dropna=count_dropna)
columns = DataFrame()
for column in nulls_df.columns:
    columns[column] = [nulls_df[column][row] for row in expected_rows]
index = MultiIndex.from_frame(columns)
expected = Series(data=expected_values, index=index)
tm.assert_series_equal(result, expected)
