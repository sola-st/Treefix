# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_batch_gather_op_test.py
params = ragged_factory_ops.constant(params)
indices = ragged_factory_ops.constant(indices)
with self.assertRaises(error):
    _ = ragged_batch_gather_with_default_op.batch_gather_with_default(
        params, indices, default_value)
