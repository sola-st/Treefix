# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_op_test.py
params = ragged_factory_ops.constant(params, ragged_rank=params_ragged_rank)
indices = ragged_factory_ops.constant(
    indices, ragged_rank=indices_ragged_rank)
actual = ragged_gather_ops.gather(
    params, indices, axis=axis, batch_dims=batch_dims)
self.assertAllEqual(actual, self._str_to_bytes(expected))
