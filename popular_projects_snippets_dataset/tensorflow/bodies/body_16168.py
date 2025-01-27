# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_row_lengths_op_test.py
rt = ragged_factory_ops.constant(rt_input)
with self.assertRaisesRegex(exception, message):
    rt.row_lengths(axis)
