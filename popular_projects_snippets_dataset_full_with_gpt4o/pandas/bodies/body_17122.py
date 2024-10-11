# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
index = ["A", "B"]
columns = "C"
table = pivot_table(
    data, values="D", index=index, columns=columns, observed=observed
)

table2 = data.pivot_table(
    values="D", index=index, columns=columns, observed=observed
)
tm.assert_frame_equal(table, table2)

# this works
pivot_table(data, values="D", index=index, observed=observed)

if len(index) > 1:
    assert table.index.names == tuple(index)
else:
    assert table.index.name == index[0]

if len(columns) > 1:
    assert table.columns.names == columns
else:
    assert table.columns.name == columns[0]

expected = data.groupby(index + [columns])["D"].agg(np.mean).unstack()
tm.assert_frame_equal(table, expected)
