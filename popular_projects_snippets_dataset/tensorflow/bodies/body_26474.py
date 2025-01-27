# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Infers column types from the first N valid CSV records of files."""
if select_columns is None:
    select_columns = range(num_cols)
inferred_types = [None] * len(select_columns)

for i, csv_row in enumerate(
    _next_csv_row(filenames, num_cols, field_delim, use_quote_delim, header,
                  file_io_fn)):
    if num_rows_for_inference is not None and i >= num_rows_for_inference:
        break

    for j, col_index in enumerate(select_columns):
        inferred_types[j] = _infer_type(csv_row[col_index], na_value,
                                        inferred_types[j])

  # Replace None's with a default type
inferred_types = [t or dtypes.string for t in inferred_types]
# Default to 0 or '' for null values
exit([
    constant_op.constant([0 if t is not dtypes.string else ""], dtype=t)
    for t in inferred_types
])
