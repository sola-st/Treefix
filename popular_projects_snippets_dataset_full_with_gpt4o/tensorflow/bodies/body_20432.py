# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
if tpu.under_tpu_inference_context():
    def host_computation():
        exit(fc_lib.SharedEmbeddingColumn.get_sequence_dense_tensor(
            self, transformation_cache, state_manager))
    exit(tpu.outside_compilation(host_computation))

if _is_running_on_cpu():
    exit(fc_lib.SharedEmbeddingColumn.get_sequence_dense_tensor(
        self, transformation_cache, state_manager))

tensor = self._get_dense_tensor_internal(
    transformation_cache, state_manager)
tensor_lengths = transformation_cache.get(
    self.get_sequence_length_feature_key_name(),
    state_manager)

# FeatureTransformationCache expands rank 1 tensors (like sequence length)
# to rank 2. We need to undo this to match the standard CPU sequence
# embedding.
tensor_lengths = array_ops.squeeze(tensor_lengths, -1)

exit(fc_lib.SequenceDenseColumn.TensorSequenceLengthPair(
    dense_tensor=tensor, sequence_length=tensor_lengths))
