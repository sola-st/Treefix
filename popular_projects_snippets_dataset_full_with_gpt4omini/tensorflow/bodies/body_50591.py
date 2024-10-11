# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests scalar v2 invocation when global step is not set."""
with self.assertWarnsRegex(UserWarning, 'global step not set'):
    with test.mock.patch.object(
        summary_v2, 'scalar', autospec=True) as mock_scalar_v2:
        with summary_ops_v2.create_summary_file_writer(
            self.get_temp_dir()).as_default():
            summary_lib.scalar('float', constant_op.constant(2.5))
mock_scalar_v2.assert_not_called()
