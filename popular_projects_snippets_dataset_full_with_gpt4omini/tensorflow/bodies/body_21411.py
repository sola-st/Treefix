# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_ops_test.py
"""Tests for the load_embedding_initializer wrapper."""
embedding_loading_initializer = (checkpoint_ops._load_embedding_initializer(
    new_vocab_file=self.new_feature_vocab_file,
    old_vocab_file=self.old_feature_vocab_file,
    new_vocab_size=5,
    embedding_dim=16,
    embedding_tensor_name='some_scope/embeddings',
    ckpt_path=[self.checkpoint_file],
    num_oov_buckets=1,
    initializer=self.initializer))

# The new weight matrix is of size
# [5 feature vocab + 1 feature OOV, 16 (embedding dimension)], where the
# last vocab row (2nd last row) is newly initialized (wasn't found in
# previous vocab) and the actual last row is OOV and also newly initialized.
# Use a partitioned variable to confirm that the offset logic works.
expected_remapped_embeddings = np.concatenate(
    [
        np.reshape(range(64), [4, 16]),
        np.reshape([self.init_val] * 32, [2, 16]),
    ],
    axis=0)
remapped_embeddings = variable_scope.get_variable(
    name='embedding/obtained_embedding_matrix',
    shape=[6, 16],
    initializer=embedding_loading_initializer,
    partitioner=partitioned_variables.fixed_size_partitioner(2))

with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(expected_remapped_embeddings,
                        remapped_embeddings.as_tensor())
