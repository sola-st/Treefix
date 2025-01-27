# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
spec1 = RaggedTensorSpec([32, None, None],
                         dtypes.float32,
                         2,
                         flat_values_spec=WrappedTensor.Spec(
                             tensor_spec.TensorSpec([None, None],
                                                    dtypes.float32)))
spec2 = RaggedTensorSpec(
    None,
    dtypes.float32,
    2,
    flat_values_spec=WrappedTensor.Spec(
        tensor_spec.TensorSpec(None, dtypes.float32)))
spec3 = RaggedTensorSpec(
    None,
    dtypes.int32,
    1,
    flat_values_spec=WrappedTensor.Spec(
        tensor_spec.TensorSpec(None, dtypes.int32)))
spec4 = RaggedTensorSpec([None],
                         dtypes.int32,
                         0,
                         flat_values_spec=WrappedTensor.Spec(
                             tensor_spec.TensorSpec(None, dtypes.int32)))
spec5 = RaggedTensorSpec([None], dtypes.int32, 0)

self.assertTrue(spec1.is_compatible_with(spec2))
self.assertFalse(spec1.is_compatible_with(spec3))
self.assertFalse(spec1.is_compatible_with(spec4))
self.assertFalse(spec2.is_compatible_with(spec3))
self.assertFalse(spec2.is_compatible_with(spec4))
self.assertFalse(spec3.is_compatible_with(spec4))
self.assertFalse(spec4.is_compatible_with(spec5))
value = constant_op.constant([1, 2, 3])
self.assertFalse(spec4.is_compatible_with(value))
self.assertTrue(spec4.is_compatible_with(WrappedTensor(value)))
