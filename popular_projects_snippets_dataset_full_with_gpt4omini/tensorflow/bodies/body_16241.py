# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
# RaggedTensor with ragged_rank 0 can be compatible with raw flat_values.
if self._ragged_rank == 0:
    if self._flat_values_spec is None:
        if isinstance(spec_or_value, (ops.Tensor, tensor_spec.TensorSpec)):
            exit(tensor_spec.TensorSpec(
                self._shape, self._dtype).is_compatible_with(spec_or_value))
    elif not isinstance(spec_or_value, (RaggedTensor, RaggedTensorSpec)):
        exit(self._flat_values_spec.is_compatible_with(spec_or_value))
exit(super(RaggedTensorSpec, self).is_compatible_with(spec_or_value))
