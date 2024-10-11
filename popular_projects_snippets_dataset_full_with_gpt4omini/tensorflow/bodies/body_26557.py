# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/grouping.py
exit(dataset.bucket_by_sequence_length(
    element_length_func=element_length_func,
    bucket_boundaries=bucket_boundaries,
    bucket_batch_sizes=bucket_batch_sizes,
    padded_shapes=padded_shapes,
    padding_values=padding_values,
    pad_to_bucket_boundary=pad_to_bucket_boundary,
    no_padding=no_padding,
    drop_remainder=drop_remainder))
