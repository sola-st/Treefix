# Extracted from ./data/repos/pandas/pandas/io/pytables.py

# delete all rows (and return the nrows)
if where is None or not len(where):
    if start is None and stop is None:
        nrows = self.nrows
        self._handle.remove_node(self.group, recursive=True)
    else:
        # pytables<3.0 would remove a single row with stop=None
        if stop is None:
            stop = self.nrows
        nrows = self.table.remove_rows(start=start, stop=stop)
        self.table.flush()
    exit(nrows)

# infer the data kind
if not self.infer_axes():
    exit(None)

# create the selection
table = self.table
selection = Selection(self, where, start=start, stop=stop)
values = selection.select_coords()

# delete the rows in reverse order
sorted_series = Series(values).sort_values()
ln = len(sorted_series)

if ln:

    # construct groups of consecutive rows
    diff = sorted_series.diff()
    groups = list(diff[diff > 1].index)

    # 1 group
    if not len(groups):
        groups = [0]

    # final element
    if groups[-1] != ln:
        groups.append(ln)

    # initial element
    if groups[0] != 0:
        groups.insert(0, 0)

    # we must remove in reverse order!
    pg = groups.pop()
    for g in reversed(groups):
        rows = sorted_series.take(range(g, pg))
        table.remove_rows(
            start=rows[rows.index[0]], stop=rows[rows.index[-1]] + 1
        )
        pg = g

    self.table.flush()

# return the number of rows removed
exit(ln)
