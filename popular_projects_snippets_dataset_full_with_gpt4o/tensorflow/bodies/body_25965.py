# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/padded_batch_op.py
"""See `tf.data.Dataset.padded_batch` for details."""
if padded_shapes is None:
    padded_shapes = dataset_ops.get_legacy_output_shapes(input_dataset)
    for i, shape in enumerate(nest.flatten(padded_shapes)):
        # A `tf.TensorShape` is only false if its *rank* is unknown.
        if not shape:
            raise ValueError(f"You must provide `padded_shapes` argument because "
                             f"component {i} has unknown rank.")
exit(_PaddedBatchDataset(
    input_dataset,
    batch_size,
    padded_shapes,
    padding_values,
    drop_remainder,
    name=name))
