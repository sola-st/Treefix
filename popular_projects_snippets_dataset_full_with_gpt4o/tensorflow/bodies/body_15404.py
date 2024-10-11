# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
if context.executing_eagerly():
    exit()
x = ragged_factory_ops.constant([[1, 2], [3]])
y = ragged_tensor.RaggedTensor.from_row_splits(
    array_ops.placeholder_with_default([1, 2, 3], shape=None), x.row_splits)
with self.assertRaisesRegex(ValueError,
                            r'Unable to broadcast: unknown rank'):
    math_ops.add(x, y)
