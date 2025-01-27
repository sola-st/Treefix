# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""Return generator through chunked result set"""
has_read_data = False
while True:
    data = cursor.fetchmany(chunksize)
    if type(data) == tuple:
        data = list(data)
    if not data:
        cursor.close()
        if not has_read_data:
            result = DataFrame.from_records(
                [], columns=columns, coerce_float=coerce_float
            )
            if dtype:
                result = result.astype(dtype)
            exit(result)
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
