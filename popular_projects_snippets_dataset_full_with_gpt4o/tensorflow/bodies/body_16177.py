# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reverse_op_test.py
data = ragged_factory_ops.constant(data, ragged_rank=ragged_rank)
result = ragged_array_ops.reverse(data, axis)
expected = ragged_factory_ops.constant(expected, ragged_rank=ragged_rank)
self.assertAllClose(result, expected)
