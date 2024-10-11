# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# column specified
result = data.pivot_table(
    values="D", index=["A", "B"], columns="C", margins=True, aggfunc=np.mean
)
self._check_output(result, "D", data)

# Set a different margins_name (not 'All')
result = data.pivot_table(
    values="D",
    index=["A", "B"],
    columns="C",
    margins=True,
    aggfunc=np.mean,
    margins_name="Totals",
)
self._check_output(result, "D", data, margins_col="Totals")

# no column specified
table = data.pivot_table(
    index=["A", "B"], columns="C", margins=True, aggfunc=np.mean
)
for value_col in table.columns.levels[0]:
    self._check_output(table[value_col], value_col, data)
