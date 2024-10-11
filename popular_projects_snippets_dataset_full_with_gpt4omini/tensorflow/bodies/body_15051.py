# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
with self.assertRaisesRegex(
    TypeError, '`nested_row_splits` must be a list of Tensors'):
    RaggedTensor.from_nested_row_splits(
        [1, 2], constant_op.constant([[0, 1, 2], [0, 1, 2]], dtypes.int64))
