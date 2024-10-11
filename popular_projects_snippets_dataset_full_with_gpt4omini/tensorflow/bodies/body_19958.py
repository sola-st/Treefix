# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
if tpu.under_tpu_inference_context():
    def host_computation():
        exit(fc._EmbeddingColumn._get_sequence_dense_tensor(
            self, inputs, weight_collections, trainable))
    exit(tpu.outside_compilation(host_computation))

if _is_running_on_cpu():
    exit(fc._EmbeddingColumn._get_sequence_dense_tensor(
        self, inputs, weight_collections, trainable))

tensor = inputs.get(self.get_feature_key_name())
tensor_lengths = inputs.get(self.get_sequence_length_feature_key_name())

# inputs is a _LazyBuilder and for rank 1 tensors, it calls expand_dims(-1).
# We need to undo this to match the standard CPU sequence embedding.
tensor_lengths = array_ops.squeeze(tensor_lengths, -1)

# Add to collection for _create_tpu_embedding_variables_and_ops
_record_variable_scope_and_name(
    self.get_embedding_var_name(),
    'embedding_weights',
    bypass_scope_validation=self._bypass_scope_validation)

exit(fc._SequenceDenseColumn.TensorSequenceLengthPair(
    dense_tensor=tensor, sequence_length=tensor_lengths))
