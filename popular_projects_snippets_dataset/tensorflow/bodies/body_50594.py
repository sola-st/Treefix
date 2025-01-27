# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests scalar v2 invocation when v1 step is set."""
global_step = training_util.create_global_step()
global_step.assign(1024)
with test.mock.patch.object(
    summary_v2, 'scalar', autospec=True) as mock_scalar_v2:
    with summary_ops_v2.create_summary_file_writer(
        self.get_temp_dir()).as_default():
        i = constant_op.constant(2.5)
        tensor = summary_lib.scalar('float', i)
    # Returns empty string.
self.assertEqual(tensor.numpy(), b'')
self.assertEqual(tensor.dtype, dtypes.string)
mock_scalar_v2.assert_called_once_with('float', data=i, step=1024)
