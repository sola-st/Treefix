# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests the op's load and remap where there are missing entries."""
init_val = 42
remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=[2, -1, 0],
    col_remapping=[1, -1],
    initializing_values=[init_val] * 4,
    num_rows=3,
    num_cols=2)

expected_remapped_matrix = np.reshape(
    [33, init_val, init_val, init_val, 1, init_val], [3, 2])

with self.cached_session():
    self.assertAllClose(expected_remapped_matrix,
                        self.evaluate(remapped_matrix))
