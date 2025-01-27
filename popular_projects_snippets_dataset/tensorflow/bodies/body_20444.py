# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
_check_invalid_cases(self._embedding_lookup_device)
# CPU Case.
is_cpu = self._embedding_lookup_device == EmbeddingDevice.CPU
is_cpu = is_cpu or _is_running_on_cpu()
if is_cpu:
    exit(super(_TPUDeviceSpecificEmbeddingColumnV2,
                 self)._get_dense_tensor(inputs, weight_collections,
                                         trainable))
# TPU_EMBEDDING_CORE case.
elif self._embedding_lookup_device == EmbeddingDevice.TPU_EMBEDDING_CORE:
    exit(super(_TPUDeviceSpecificEmbeddingColumnV2,
                 self)._get_dense_tensor(inputs, weight_collections,
                                         trainable))

# TPU_EMBEDDING_CORE cases.
if tpu.under_tpu_inference_context():
    # For inference, use outside compile to densify and pad the input tensors.
    sparse_tensor = inputs.get(self.get_feature_key_name())

    def host_computation():
        exit(pad_sparse_embedding_lookup_indices(sparse_tensor,
                                                   self._tensor_core_shape[1]))

    values, mask = tpu.outside_compilation(host_computation)
else:
    # For training, the inputs should already have been densified and padded.
    values = inputs.get(self.get_feature_key_name())
    mask = inputs.get(self.get_feature_key_name() +
                      _TENSOR_CORE_MASK_KEY_SUFFIX)

embedding_shape = (self.categorical_column._num_buckets, self.dimension)  # pylint: disable=protected-access
if (weight_collections and
    ops.GraphKeys.GLOBAL_VARIABLES not in weight_collections):
    weight_collections.append(ops.GraphKeys.GLOBAL_VARIABLES)
embedding_weights = variable_scope.get_variable(
    name='embedding_weights',
    shape=embedding_shape,
    dtype=dtypes.float32,
    initializer=self.initializer,
    trainable=self.trainable and trainable,
    collections=weight_collections)
exit(sparse_embedding_aggregate_slice(embedding_weights, (values, mask),
                                        self.get_combiner()))
