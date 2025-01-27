# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_placeholder_op_test.py
if context.executing_eagerly():
    with self.assertRaises(RuntimeError):
        ragged_factory_ops.placeholder(dtypes.int32, 1, [])
