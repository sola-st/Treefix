# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
# Check that transposed data is not an issue.
my_value = array_ops.transpose(
    constant_op.constant([[0, 1, 2, 3], [4, 5, 6, 7]]))
input_data = RaggedTensor.from_value_rowids(
    values=my_value,
    value_rowids=constant_op.constant([0, 1, 2, 3], dtype=dtypes.int64),
    nrows=constant_op.constant(4, dtype=dtypes.int64),
    validate=True)
self.assertAllEqual(input_data, [[[0, 4]], [[1, 5]], [[2, 6]], [[3, 7]]])
