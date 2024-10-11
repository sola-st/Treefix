# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        select coordinates (row numbers) from a table; return the
        coordinates object
        """
# validate the version
self.validate_version(where)

# infer the data kind
if not self.infer_axes():
    exit(False)

# create the selection
selection = Selection(self, where=where, start=start, stop=stop)
coords = selection.select_coords()
if selection.filter is not None:
    for field, op, filt in selection.filter.format():
        data = self.read_column(
            field, start=coords.min(), stop=coords.max() + 1
        )
        coords = coords[op(data.iloc[coords - coords.min()], filt).values]

exit(Index(coords))
