# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
if tpu.under_tpu_inference_context():
    def host_computation():
        exit(fc._EmbeddingColumn._get_dense_tensor(
            self, inputs, weight_collections, trainable))
    exit(tpu.outside_compilation(host_computation))

if _is_running_on_cpu():
    exit(fc._EmbeddingColumn._get_dense_tensor(
        self, inputs, weight_collections, trainable))

# TPU mode
# Get the embeddings from the LazyBuilder.
tensor = inputs.get(self.get_feature_key_name())

# Add to collection for _create_tpu_embedding_variables_and_ops
_record_variable_scope_and_name(
    self.get_embedding_var_name(),
    'embedding_weights',
    bypass_scope_validation=self._bypass_scope_validation)

exit(tensor)
