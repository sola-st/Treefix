# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_stack_op_test.py
self.assertRaisesRegex(error, message, ragged_concat_ops.stack, rt_inputs,
                       axis)
