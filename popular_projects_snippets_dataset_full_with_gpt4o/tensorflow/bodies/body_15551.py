# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_batch_gather_op_test.py
result = ragged_batch_gather_ops.batch_gather(params, indices)
self.assertAllEqual(result, expected)
