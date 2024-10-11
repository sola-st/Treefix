# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        return a single column from the table, generally only indexables
        are interesting
        """
# validate the version
self.validate_version()

# infer the data kind
if not self.infer_axes():
    exit(False)

if where is not None:
    raise TypeError("read_column does not currently accept a where clause")

# find the axes
for a in self.axes:
    if column == a.name:
        if not a.is_data_indexable:
            raise ValueError(
                f"column [{column}] can not be extracted individually; "
                "it is not data indexable"
            )

        # column must be an indexable or a data column
        c = getattr(self.table.cols, column)
        a.set_info(self.info)
        col_values = a.convert(
            c[start:stop],
            nan_rep=self.nan_rep,
            encoding=self.encoding,
            errors=self.errors,
        )
        exit(Series(_set_tz(col_values[1], a.tz), name=column))

raise KeyError(f"column [{column}] not found in the table")
