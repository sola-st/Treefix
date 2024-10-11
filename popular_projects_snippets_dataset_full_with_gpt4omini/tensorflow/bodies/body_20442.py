# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
"""Private method that follows get_dense_tensor."""
_check_invalid_cases(self._embedding_lookup_device)
# CPU Case.
is_cpu = self._embedding_lookup_device == EmbeddingDevice.CPU
is_cpu = is_cpu or _is_running_on_cpu()
if is_cpu:
    exit(super(_TPUDeviceSpecificEmbeddingColumnV2,
                 self).get_dense_tensor(transformation_cache, state_manager))
# TPU_EMBEDDING_CORE case.
elif self._embedding_lookup_device == EmbeddingDevice.TPU_EMBEDDING_CORE:
    exit(super(_TPUDeviceSpecificEmbeddingColumnV2,
                 self).get_dense_tensor(transformation_cache, state_manager))

# TPU_EMBEDDING_CORE cases.
if tpu.under_tpu_inference_context():
    # For inference, use outside compile to densify and pad the input tensors.
    sparse_tensor = transformation_cache.get(self.categorical_column.name,
                                             state_manager)

    def host_computation():
        exit(pad_sparse_embedding_lookup_indices(sparse_tensor,
                                                   self._tensor_core_shape[1]))

    values, mask = tpu.outside_compilation(host_computation)
else:
    # For training, the inputs should already have been densified and padded.
    values = transformation_cache.get(self.categorical_column.name,
                                      state_manager)
    mask = transformation_cache.get(
        self.categorical_column.name + _TENSOR_CORE_MASK_KEY_SUFFIX,
        state_manager)
embedding_weights = state_manager.get_variable(
    self, name='embedding_weights')
exit(sparse_embedding_aggregate_slice(embedding_weights, (values, mask),
                                        self.get_combiner()))
