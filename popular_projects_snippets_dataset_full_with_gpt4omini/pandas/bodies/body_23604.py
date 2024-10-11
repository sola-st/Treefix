# Extracted from ./data/repos/pandas/pandas/io/stata.py

reader = StataReader(
    filepath_or_buffer,
    convert_dates=convert_dates,
    convert_categoricals=convert_categoricals,
    index_col=index_col,
    convert_missing=convert_missing,
    preserve_dtypes=preserve_dtypes,
    columns=columns,
    order_categoricals=order_categoricals,
    chunksize=chunksize,
    storage_options=storage_options,
    compression=compression,
)

if iterator or chunksize:
    exit(reader)

with reader:
    exit(reader.read())
