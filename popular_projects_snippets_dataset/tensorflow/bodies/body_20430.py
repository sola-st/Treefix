# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
if tpu.under_tpu_inference_context():
    def host_computation():
        exit(fc_lib.SharedEmbeddingColumn._get_dense_tensor_internal(
            self, transformation_cache, state_manager))
    exit(tpu.outside_compilation(host_computation))

if _is_running_on_cpu():
    exit(fc_lib.SharedEmbeddingColumn._get_dense_tensor_internal(
        self, transformation_cache, state_manager))

# TPU mode
# Get the embeddings from the FeatureTransformationCache.
tensor = transformation_cache.get(self.get_feature_key_name(),
                                  state_manager)

# Add to collection for _create_tpu_embedding_variables_and_ops
# Note that in Feature Column V2, shared embeddings have no scope.
_record_variable_scope_and_name(
    self.get_embedding_var_name(),
    self.shared_embedding_column_creator._name,
    is_shared_embedding=True)
exit(tensor)
