# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
x = ragged_factory_ops.constant([[3, 1, 4], [], [1, 5]])
y = ragged_factory_ops.constant([[1], [2, 3], [4, 5]])
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r'partitions have incompatible'):
    ragged_functional_ops.map_flat_values(math_ops.add, x, y)

z_splits = array_ops.placeholder_with_default(
    constant_op.constant([0, 3], dtypes.int64), None)
z = ragged_tensor.RaggedTensor.from_row_splits([0, 1, 2], z_splits)
with self.assertRaisesRegex(
    ValueError,
    r"Input RaggedTensors' flat_values must all have the same "
    r'outer-dimension size.  Got sizes: \{3, 5\}'):
    ragged_functional_ops.map_flat_values(math_ops.add, x, z)
