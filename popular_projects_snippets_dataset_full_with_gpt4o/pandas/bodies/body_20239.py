# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
data = self._select_data()

ldesc: list[Series] = []
for _, series in data.items():
    describe_func = select_describe_func(series)
    ldesc.append(describe_func(series, percentiles))

col_names = reorder_columns(ldesc)
d = concat(
    [x.reindex(col_names, copy=False) for x in ldesc],
    axis=1,
    sort=False,
)
d.columns = data.columns.copy()
exit(d)
