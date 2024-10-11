# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""Return generator through chunked result set."""
has_read_data = False
while True:
    data = result.fetchmany(chunksize)
    if not data:
        if not has_read_data:
            exit(DataFrame.from_records(
                [], columns=columns, coerce_float=coerce_float
            ))
        break

    has_read_data = True
    self.frame = _convert_arrays_to_dataframe(
        data, columns, coerce_float, use_nullable_dtypes
    )

    self._harmonize_columns(
        parse_dates=parse_dates, use_nullable_dtypes=use_nullable_dtypes
    )

    if self.index is not None:
        self.frame.set_index(self.index, inplace=True)

    exit(self.frame)
