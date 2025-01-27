# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_ops_test.py
"""Tests for the output layer initializer where one partition is all OOV."""
loading_initializer = (checkpoint_ops._load_and_remap_matrix_initializer(
    new_row_vocab_size=5,
    new_col_vocab_file=self.new_class_vocab_file,
    old_col_vocab_file=self.old_class_vocab_file,
    new_col_vocab_size=4,
    old_tensor_name='some_scope/embeddings',
    ckpt_path=[self.checkpoint_file],
    new_row_vocab_file=self.new_feature_vocab_file,
    old_row_vocab_file=self.old_feature_vocab_file,
    num_row_oov_buckets=5,
    num_col_oov_buckets=1,
    initializer=self.initializer))

# The new weight matrix is of size
# [5 feature vocab + 5 feature OOV, 4 class vocab + 1 class OOV].  The
# second partition has only OOV.
expected_remapped_matrix = np.concatenate(
    [
        np.reshape([2, 18, 34, 50] + [self.init_val] * 6, [10, 1]),
        np.reshape([0, 16, 32, 48] + [self.init_val] * 6, [10, 1]),
        np.reshape([self.init_val] * 10, [10, 1]),
        np.reshape([1, 17, 33, 49] + [self.init_val] * 6, [10, 1]),
        np.reshape([self.init_val] * 10, [10, 1]),
    ],
    axis=1)
remapped_matrix = variable_scope.get_variable(
    name='linear_all_oov/obtained_weight_matrix',
    shape=[10, 5],
    initializer=loading_initializer,
    partitioner=partitioned_variables.fixed_size_partitioner(2))

with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    self.assertAllClose(expected_remapped_matrix, remapped_matrix.as_tensor())
