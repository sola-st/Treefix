# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests `family` arg handling when there is an outer scope."""
with test.mock.patch.object(
    summary_v2, 'scalar', autospec=True) as mock_scalar_v2:
    with summary_ops_v2.create_summary_file_writer(
        self.get_temp_dir()).as_default(step=1):
        with ops.name_scope_v2('sea'):
            tensor = summary_lib.scalar(
                'float', constant_op.constant(3.5), family='crabnet')
    # Returns empty string.
self.assertEqual(tensor.numpy(), b'')
self.assertEqual(tensor.dtype, dtypes.string)
mock_scalar_v2.assert_called_once_with(
    'crabnet/sea/crabnet/float', data=constant_op.constant(3.5), step=1)
