# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests when all the rows are missing and need to be initialized."""
num_rows = 7
initializing_values = [42] * num_rows * self.old_num_cols
remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=[-1] * num_rows,
    col_remapping=[],
    initializing_values=initializing_values,
    num_rows=num_rows,
    num_cols=self.old_num_cols)
with self.cached_session():
    self.assertAllClose(
        np.reshape(initializing_values, (num_rows, self.old_num_cols)),
        self.evaluate(remapped_matrix))
