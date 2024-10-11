# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests that errors are raised when an ID maps to multiple new IDs.

    (This should usually not happen when using public APIs).
    """
invalid_remapping = [1, 0, 0, 0, 1, 2]

# Invalid row remapping.
remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=invalid_remapping,
    col_remapping=[],
    initializing_values=[],
    num_rows=len(invalid_remapping),
    num_cols=self.old_num_cols)
with self.cached_session(), self.assertRaises(errors.UnimplementedError):
    self.evaluate(remapped_matrix)

# Invalid column remapping.
remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=list(range(self.old_num_rows)),
    col_remapping=invalid_remapping,
    initializing_values=[],
    num_rows=self.old_num_rows,
    num_cols=len(invalid_remapping))
with self.cached_session(), self.assertRaises(errors.UnimplementedError):
    self.evaluate(remapped_matrix)
