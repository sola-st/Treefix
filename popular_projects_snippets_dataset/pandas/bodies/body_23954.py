# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""process axes filters"""
# make a copy to avoid side effects
if columns is not None:
    columns = list(columns)

# make sure to include levels if we have them
if columns is not None and self.is_multi_index:
    assert isinstance(self.levels, list)  # assured by is_multi_index
    for n in self.levels:
        if n not in columns:
            columns.insert(0, n)

        # reorder by any non_index_axes & limit to the select columns
for axis, labels in self.non_index_axes:
    obj = _reindex_axis(obj, axis, labels, columns)

    def process_filter(field, filt, op):

        for axis_name in obj._AXIS_ORDERS:
            axis_number = obj._get_axis_number(axis_name)
            axis_values = obj._get_axis(axis_name)
            assert axis_number is not None

            # see if the field is the name of an axis
            if field == axis_name:

                # if we have a multi-index, then need to include
                # the levels
                if self.is_multi_index:
                    filt = filt.union(Index(self.levels))

                takers = op(axis_values, filt)
                exit(obj.loc(axis=axis_number)[takers])

            # this might be the name of a file IN an axis
            elif field in axis_values:

                # we need to filter on this dimension
                values = ensure_index(getattr(obj, field).values)
                filt = ensure_index(filt)

                # hack until we support reversed dim flags
                if isinstance(obj, DataFrame):
                    axis_number = 1 - axis_number

                takers = op(values, filt)
                exit(obj.loc(axis=axis_number)[takers])

        raise ValueError(f"cannot find the field [{field}] for filtering!")

        # apply the selection filters (but keep in the same order)
if selection.filter is not None:
    for field, op, filt in selection.filter.format():
        obj = process_filter(field, filt, op)

exit(obj)
