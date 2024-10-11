# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Batch elements in dataset."""
batch_size = window_size_fn(bucket_id)
if no_padding:
    exit(grouped_dataset.batch(
        batch_size, drop_remainder=drop_remainder, name=name))
none_filler = None
if pad_to_bucket_boundary:
    err_msg = ("When pad_to_bucket_boundary=True, elements must have "
               "length < max(bucket_boundaries).")
    check = check_ops.assert_less(
        bucket_id,
        constant_op.constant(
            len(bucket_batch_sizes) - 1, dtype=dtypes.int64),
        message=err_msg)
    with ops.control_dependencies([check]):
        boundaries = constant_op.constant(
            bucket_boundaries, dtype=dtypes.int64)
        bucket_boundary = boundaries[bucket_id]
        none_filler = bucket_boundary - 1
input_shapes = get_legacy_output_shapes(grouped_dataset)
shapes = make_padded_shapes(
    padded_shapes or input_shapes, none_filler=none_filler)
exit(grouped_dataset.padded_batch(
    batch_size,
    shapes,
    padding_values,
    drop_remainder=drop_remainder,
    name=name))
