# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
exit(dataset_ops.DatasetV1Adapter(make_batched_features_dataset_v2(
    file_pattern, batch_size, features, reader, label_key, reader_args,
    num_epochs, shuffle, shuffle_buffer_size, shuffle_seed,
    prefetch_buffer_size, reader_num_threads, parser_num_threads,
    sloppy_ordering, drop_final_batch)))
