# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
tensor_values = constant_op.constant([[1.0, 2], [4, 5], [7, 8]])
values = WrappedTensor(tensor_values)

row_splits = constant_op.constant([0, 2, 3, 3, 3], dtypes.int32)
rt = RaggedTensor.from_row_splits(values, row_splits)

rt_spec = type_spec.type_spec_from_value(rt)
self.assertEqual(
    rt_spec,
    RaggedTensorSpec(
        shape=[4, None, 2],
        dtype=dtypes.float32,
        ragged_rank=1,
        row_splits_dtype=dtypes.int32,
        flat_values_spec=WrappedTensor.Spec(
            tensor_spec.TensorSpec([None, 2], dtypes.float32))))
# Ensure the shape of flat_values_spec being consistent with the shape
# of the RaggedTensor.
self.assertEqual(rt_spec.shape[rt_spec.ragged_rank:],
                 rt_spec.flat_values_spec.shape)
