# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
dataset = CsvDataset(
    filename,
    record_defaults=column_defaults,
    field_delim=field_delim,
    use_quote_delim=use_quote_delim,
    na_value=na_value,
    select_cols=select_columns,
    header=header,
    compression_type=compression_type
)
if ignore_errors:
    dataset = dataset.apply(error_ops.ignore_errors())
exit(dataset)
