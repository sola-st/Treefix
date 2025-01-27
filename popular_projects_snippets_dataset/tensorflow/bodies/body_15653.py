# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
with self.assertRaisesRegex(exception, message):
    ragged_array_ops.cross(inputs)
