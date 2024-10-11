# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests the op's load and remap where there are no missing entries."""

# No column remapping, new weight matrix has second row, then first row.
row_remapping = [1, 0]
remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=row_remapping,
    col_remapping=[],
    initializing_values=[],
    num_rows=2,
    num_cols=self.old_num_cols)
with self.cached_session():
    self.assertAllClose(self.matrix_value[row_remapping],
                        self.evaluate(remapped_matrix))

# No row remapping, new weight matrix has third col, then first col.
row_remapping = list(range(self.old_num_rows))
col_remapping = [2, 0]
remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=row_remapping,
    col_remapping=col_remapping,
    initializing_values=[],
    num_rows=len(row_remapping),
    num_cols=len(col_remapping))
with self.cached_session():
    self.assertAllClose(self.matrix_value[row_remapping][:, col_remapping],
                        self.evaluate(remapped_matrix))

# Both row and column remappings.
row_remapping = [1, 0, 4]
col_remapping = [1, 15]
remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=row_remapping,
    col_remapping=col_remapping,
    initializing_values=[],
    num_rows=len(row_remapping),
    num_cols=len(col_remapping))
with self.cached_session():
    self.assertAllClose(self.matrix_value[row_remapping][:, col_remapping],
                        self.evaluate(remapped_matrix))
