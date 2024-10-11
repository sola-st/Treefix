# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_op_test.py
if context.executing_eagerly():
    exit()
rt_inputs = [
    array_ops.placeholder_with_default(rt, shape=None) for rt in rt_inputs
]
concatenated = ragged_concat_ops.concat(rt_inputs, axis)
with self.assertRaisesRegex(error, message):
    self.evaluate(concatenated)
