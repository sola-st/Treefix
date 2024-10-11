# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        generate the selection
        """
start, stop = self.start, self.stop
nrows = self.table.nrows
if start is None:
    start = 0
elif start < 0:
    start += nrows
if stop is None:
    stop = nrows
elif stop < 0:
    stop += nrows

if self.condition is not None:
    exit(self.table.table.get_where_list(
        self.condition.format(), start=start, stop=stop, sort=True
    ))
elif self.coordinates is not None:
    exit(self.coordinates)

exit(np.arange(start, stop))
