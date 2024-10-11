# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_bitcast_op_test.py
result = ragged_array_ops.bitcast(inputs, outputs.dtype, name)
self.assertEqual(result.dtype, outputs.dtype)
self.assertEqual(result.ragged_rank, outputs.ragged_rank)
self.assertAllEqual(result, outputs)
