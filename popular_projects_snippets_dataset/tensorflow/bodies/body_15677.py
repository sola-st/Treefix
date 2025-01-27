# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
tensor_values = constant_op.constant(
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
values = WrappedTensor(tensor_values)

row_splits = constant_op.constant([0, 2, 2, 5, 6, 8], dtypes.int64)
rt = RaggedTensor.from_row_splits(values, row_splits)
self.assertIsInstance(rt.values, WrappedTensor)
self.assertAllEqual(rt.values.value, tensor_values)
self.assertAllEqual(rt.row_splits, row_splits)

row_starts = constant_op.constant([0, 2, 2, 5, 6], dtypes.int64)
rt = RaggedTensor.from_row_starts(values, row_starts)
self.assertIsInstance(rt.values, WrappedTensor)
self.assertAllEqual(rt.values.value, tensor_values)
self.assertAllEqual(rt.row_starts(), row_starts)

row_limits = constant_op.constant([2, 2, 5, 6, 8], dtypes.int64)
rt = RaggedTensor.from_row_limits(values, row_limits)
self.assertIsInstance(rt.values, WrappedTensor)
self.assertAllEqual(rt.values.value, tensor_values)
self.assertAllEqual(rt.row_limits(), row_limits)

row_lengths = constant_op.constant([2, 0, 3, 1, 2], dtypes.int64)
rt = RaggedTensor.from_row_lengths(values, row_lengths)
self.assertIsInstance(rt.values, WrappedTensor)
self.assertAllEqual(rt.values.value, tensor_values)
self.assertAllEqual(rt.row_lengths(), row_lengths)

rt = RaggedTensor.from_uniform_row_length(values, 4)
self.assertIsInstance(rt.values, WrappedTensor)
self.assertAllEqual(rt.values.value, tensor_values)
self.assertAllEqual(rt.uniform_row_length, 4)
