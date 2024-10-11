# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
if tpu.under_tpu_inference_context():
    def host_computation():
        exit(fc_lib.EmbeddingColumn.get_dense_tensor(
            self, transformation_cache, state_manager))
    exit(tpu.outside_compilation(host_computation))

if _is_running_on_cpu():
    exit(fc_lib.EmbeddingColumn.get_dense_tensor(
        self, transformation_cache, state_manager))

# TPU mode
# Get the embeddings from the FeatureTransformationCache.
tensor = transformation_cache.get(self.get_feature_key_name(),
                                  state_manager)

exit(tensor)
