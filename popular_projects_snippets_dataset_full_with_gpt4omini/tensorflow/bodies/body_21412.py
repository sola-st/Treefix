# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_ops_test.py
"""Tests for the large OOV case for load_embedding_initializer wrapper."""
self.new_feature_vocab_file = os.path.join(
    self.get_temp_dir(), 'new_feature_vocab.txt')
with open(self.new_feature_vocab_file, 'w') as f:
    f.write('\n'.join(['one', 'zero', 'two', 'four']) + '\n')

# Checkpoint has 5 entries, 3 of which correspond to OOV.
self.old_feature_vocab_file = os.path.join(
    self.get_temp_dir(), 'old_feature_vocab.txt')
with open(self.old_feature_vocab_file, 'w') as f:
    f.write('\n'.join(['zero', 'one']) + '\n')

embedding_loading_initializer = (checkpoint_ops._load_embedding_initializer(
    new_vocab_file=self.new_feature_vocab_file,
    old_vocab_file=self.old_feature_vocab_file,
    new_vocab_size=4,
    embedding_dim=16,
    embedding_tensor_name='some_scope/embeddings',
    ckpt_path=[self.checkpoint_file],
    num_oov_buckets=5,
    initializer=self.initializer))

# The new weight matrix is of size
# [4 feature vocab + 5 feature OOV, 16 (embedding dimension)], where the
# 3rd and 4th rows are not found in the old vocabulary and therefore newly
# initialized.  The last five rows are OOV and also newly initialized.
# Use a partitioned variable to confirm that the offset logic works.
expected_remapped_embeddings = np.concatenate(
    [
        np.reshape(range(16, 32), [1, 16]),
        np.reshape(range(16), [1, 16]),
        np.reshape([self.init_val] * 112, [7, 16]),
    ],
    axis=0)
remapped_embeddings = variable_scope.get_variable(
    name='embedding/obtained_embedding_matrix',
    shape=[9, 16],
    initializer=embedding_loading_initializer,
    partitioner=partitioned_variables.fixed_size_partitioner(2))

with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(expected_remapped_embeddings,
                        remapped_embeddings.as_tensor())
