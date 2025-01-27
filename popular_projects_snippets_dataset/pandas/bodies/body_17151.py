# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
col_margins = result.loc[result.index[:-1], margins_col]
expected_col_margins = data.groupby(index)[values_col].mean()
tm.assert_series_equal(col_margins, expected_col_margins, check_names=False)
assert col_margins.name == margins_col

result = result.sort_index()
index_margins = result.loc[(margins_col, "")].iloc[:-1]

expected_ix_margins = data.groupby(columns)[values_col].mean()
tm.assert_series_equal(index_margins, expected_ix_margins, check_names=False)
assert index_margins.name == (margins_col, "")

grand_total_margins = result.loc[(margins_col, ""), margins_col]
expected_total_margins = data[values_col].mean()
assert grand_total_margins == expected_total_margins
