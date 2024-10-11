# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
# Check that TwoCompositeSpecs are compatible if one has a nested
# RaggedTensorSpec w/ ragged_rank=0 and the other has a corresponding
# nested TensorSpec.
spec1 = TwoCompositesSpec(
    ragged_tensor.RaggedTensorSpec([10], dtypes.int32, ragged_rank=0),
    tensor_spec.TensorSpec(None, dtypes.int32))
spec2 = TwoCompositesSpec(
    tensor_spec.TensorSpec([10], dtypes.int32),
    tensor_spec.TensorSpec(None, dtypes.int32))
spec3 = TwoCompositesSpec(
    tensor_spec.TensorSpec([12], dtypes.int32),
    tensor_spec.TensorSpec(None, dtypes.int32))
self.assertTrue(spec1.is_compatible_with(spec2))
self.assertFalse(spec1.is_compatible_with(spec3))
