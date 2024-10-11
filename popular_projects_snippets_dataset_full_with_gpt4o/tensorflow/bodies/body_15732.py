# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_concat_op_test.py
if context.executing_eagerly():
    exit()
rt_inputs = [
    array_ops.placeholder(dtypes.int64),
    array_ops.placeholder(dtypes.int64)
]
self.assertRaisesRegex(
    ValueError,
    r'axis=-1 may only be negative if ndims is statically known.',
    ragged_concat_ops.concat, rt_inputs, -1)
