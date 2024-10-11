# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
x = ragged_factory_ops.constant([[1, 2]]).with_row_splits_dtype(left_dtype)
y = ragged_factory_ops.constant([[1, 2]]).with_row_splits_dtype(right_dtype)
with self.assertRaisesRegex(
    ValueError, 'Input RaggedTensors have mismatched row_splits dtypes'):
    math_ops.add(x, y)
