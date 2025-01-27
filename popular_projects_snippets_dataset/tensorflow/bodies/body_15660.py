# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_placeholder_op_test.py
if not context.executing_eagerly():
    placeholder = ragged_factory_ops.placeholder(
        dtype, ragged_rank, value_shape, name)
    result = str(placeholder).replace('?', 'None')
    self.assertEqual(result, expected)
