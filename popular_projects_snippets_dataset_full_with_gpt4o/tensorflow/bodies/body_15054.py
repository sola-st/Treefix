# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
if not context.executing_eagerly():
    with ops.Graph().as_default():
        values = constant_op.constant([1, 2, 3], dtypes.int64)
    with ops.Graph().as_default():
        splits = constant_op.constant([0, 2, 3], dtypes.int64)
    with self.assertRaisesRegex(ValueError,
                                '.* must be from the same graph as .*'):
        RaggedTensor.from_row_splits(values, splits)
