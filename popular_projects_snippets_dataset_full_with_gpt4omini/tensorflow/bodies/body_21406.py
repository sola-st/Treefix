# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_ops_test.py
"""Tests the end-to-end loading / remapping of weights."""
# _load_and_remap_matrix() is the generalized wrapper that takes in row and
# column vocabulary files, calls the relevant remappings, and returns the
# weight matrix.  Take this example to be linear multi-class by providing
# both row and column vocabularies.
remapped_matrix = checkpoint_ops._load_and_remap_matrix(
    new_row_vocab_file=self.new_feature_vocab_file,
    old_row_vocab_file=self.old_feature_vocab_file,
    num_rows_to_load=4,
    new_col_vocab_file=self.new_class_vocab_file,
    old_col_vocab_file=self.old_class_vocab_file,
    new_col_vocab_size=4,
    old_tensor_name='some_scope/embeddings',
    ckpt_path=[self.checkpoint_file],
    new_row_vocab_offset=1,
    initializer=self.initializer,
    num_row_oov_buckets=1,
    num_col_oov_buckets=1)

# [4 in vocab + 1 oov features, 4 in vocab + 1 oov classes].  The offset
# means we read from the first line.
expected_remapped_matrix = np.concatenate(
    [
        np.reshape([18, 34, 50, self.init_val, self.init_val], [5, 1]),
        np.reshape([16, 32, 48, self.init_val, self.init_val], [5, 1]),
        np.reshape([self.init_val] * 5, [5, 1]),
        np.reshape([17, 33, 49, self.init_val, self.init_val], [5, 1]),
        np.reshape([self.init_val] * 5, [5, 1])
    ],
    axis=1)

with self.cached_session():
    self.assertAllClose(expected_remapped_matrix,
                        self.evaluate(remapped_matrix))
