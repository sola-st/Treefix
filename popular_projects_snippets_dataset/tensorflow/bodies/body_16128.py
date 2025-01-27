# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_boolean_mask_op_test.py
actual = ragged_array_ops.boolean_mask(data, mask)
self.assertAllEqual(actual, expected)
