# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
splits1 = array_ops.placeholder_with_default(
    constant_op.constant([0, 3, 3, 5], dtypes.int64), None)
splits2 = array_ops.placeholder_with_default(
    constant_op.constant([0, 1, 3, 5], dtypes.int64), None)
x = ragged_tensor.RaggedTensor.from_row_splits([3, 1, 4, 1, 5], splits1)
y = ragged_tensor.RaggedTensor.from_row_splits([1, 2, 3, 4, 5], splits2)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r'partitions have incompatible'):
    self.evaluate(ragged_functional_ops.map_flat_values(math_ops.add, x, y))
