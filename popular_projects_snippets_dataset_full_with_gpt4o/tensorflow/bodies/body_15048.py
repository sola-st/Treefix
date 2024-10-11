# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
with self.assertRaisesRegex(
    TypeError, 'Argument `nested_value_rowids` must be a list of Tensors'):
    RaggedTensor.from_nested_value_rowids(
        [1, 2, 3], constant_op.constant([[0, 1, 2], [0, 1, 2]], dtypes.int64))
with self.assertRaisesRegex(
    TypeError, 'Argument `nested_nrows` must be a list of Tensors'):
    RaggedTensor.from_nested_value_rowids([1, 2, 3], [[0, 1, 2], [0, 1, 2]],
                                          constant_op.constant([3, 3]))
