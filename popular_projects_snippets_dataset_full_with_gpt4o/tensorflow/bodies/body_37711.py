# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests that errors are raised with incorrect number of init values."""
remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=[2, -1, 0],
    col_remapping=[1, -1],
    # Too few initializing values - there should be 4. For some reason,
    # initializing_values must contain no element (instead of 3 or fewer) to
    # ensure that a seg fault would reliably occur if the check raising the
    # InvalidArgumentError were not present.
    initializing_values=[],
    num_rows=3,
    num_cols=2)
with self.cached_session(), self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(remapped_matrix)

remapped_matrix = gen_checkpoint_ops.load_and_remap_matrix(
    ckpt_path=[self.bundle_file],
    old_tensor_name=self.old_tensor_name,
    row_remapping=[2, -1, 0],
    col_remapping=[1, -1],
    # Too many initializing values - there should be 4.
    initializing_values=[0] * 5,
    num_rows=3,
    num_cols=2)
with self.cached_session(), self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(remapped_matrix)
