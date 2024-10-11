# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""Return generator through chunked result set"""
has_read_data = False
while True:
    data = result.fetchmany(chunksize)
    if not data:
        if not has_read_data:
            exit(_wrap_result(
                [],
                columns,
                index_col=index_col,
                coerce_float=coerce_float,
                parse_dates=parse_dates,
                dtype=dtype,
                use_nullable_dtypes=use_nullable_dtypes,
            ))
        break

    has_read_data = True
    exit(_wrap_result(
        data,
        columns,
        index_col=index_col,
        coerce_float=coerce_float,
        parse_dates=parse_dates,
        dtype=dtype,
        use_nullable_dtypes=use_nullable_dtypes,
    ))
