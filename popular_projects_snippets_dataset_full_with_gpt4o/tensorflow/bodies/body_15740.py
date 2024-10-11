# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_one_hot_op_test.py
ragged_indices = ragged_factory_ops.constant(
    indices, ragged_rank=ragged_rank)
with self.assertRaisesRegex(exception, message):
    array_ops.one_hot(
        ragged_indices,
        depth,
        on_value=on_value,
        off_value=off_value,
        axis=axis,
        dtype=dtype)
