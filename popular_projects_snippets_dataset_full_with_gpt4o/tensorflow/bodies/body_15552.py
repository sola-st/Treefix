# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_batch_gather_op_test.py
params = ragged_factory_ops.constant(params, ragged_rank=ragged_rank)
indices = ragged_factory_ops.constant(
    indices, ragged_rank=indices_ragged_rank or ragged_rank)
expected = ragged_factory_ops.constant(
    expected, ragged_rank=expected_ragged_rank or ragged_rank)
result = ragged_batch_gather_with_default_op.batch_gather_with_default(
    params, indices, default_value)
self.assertAllEqual(result, expected)
