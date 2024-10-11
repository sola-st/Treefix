# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
exit(dataset_ops.DatasetV1Adapter(
    make_csv_dataset_v2(file_pattern, batch_size, column_names,
                        column_defaults, label_name, select_columns,
                        field_delim, use_quote_delim, na_value, header,
                        num_epochs, shuffle, shuffle_buffer_size,
                        shuffle_seed, prefetch_buffer_size,
                        num_parallel_reads, sloppy, num_rows_for_inference,
                        compression_type, ignore_errors, encoding)))
