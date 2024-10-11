# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
input_data = RaggedTensor.from_value_rowids(
    values=constant_op.constant([], dtype=dtypes.int64),
    value_rowids=constant_op.constant([], dtype=dtypes.int64),
    nrows=constant_op.constant(2, dtype=dtypes.int64),
    validate=True)
actual = input_data.to_tensor(default_value=3, shape=[2, 3])
self.assertAllEqual(actual, [[3, 3, 3], [3, 3, 3]])
