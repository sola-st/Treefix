# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_batch_gather_op_test.py
params = constant_op.constant(params)
indices = constant_op.constant(indices)
expected = constant_op.constant(expected)
result = ragged_batch_gather_with_default_op.batch_gather_with_default(
    params, indices, default_value)
self.assertAllEqual(expected, result)
