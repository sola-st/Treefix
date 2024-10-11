# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
tensor_values = constant_op.constant([[1.0, 2], [3, 4], [5, 6], [7, 8]])
row_splits = constant_op.constant([0, 2, 3, 4], dtypes.int32)
raw_rt = RaggedTensor.from_row_splits(tensor_values, row_splits)

values = WrappedTensor(tensor_values)
rt = RaggedTensor.from_row_splits(values, row_splits)

res = slice_fn(rt)
raw_res = slice_fn(raw_rt)
if is_ragged_output:
    self.assertIsInstance(res, RaggedTensor)
    self.assertIsInstance(res.flat_values, WrappedTensor)
    self.assertAllEqual(res.flat_values.value, raw_res.flat_values)
    self.assertAllTensorsEqual(res.nested_row_splits,
                               raw_res.nested_row_splits)
else:
    self.assertIsInstance(res, WrappedTensor)
    self.assertAllEqual(res.value, raw_res)
