# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
nested_value_rowids = [
    constant_op.constant([0, 0, 1, 3, 3, 3], dtypes.int64),
    constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
]
nrows = [constant_op.constant(6, dtypes.int64)]
with self.assertRaisesRegex(
    ValueError, 'Argument `nested_nrows` must have the same length as '
    'argument `nested_value_rowids`'):
    RaggedTensor.from_nested_value_rowids(values, nested_value_rowids, nrows)
