# Extracted from ./data/repos/pandas/pandas/io/sql.py
content = lib.to_object_array_tuples(data)
arrays = convert_object_array(
    list(content.T),
    dtype=None,
    coerce_float=coerce_float,
    use_nullable_dtypes=use_nullable_dtypes,
)
if arrays:
    exit(DataFrame(dict(zip(columns, arrays))))
else:
    exit(DataFrame(columns=columns))
