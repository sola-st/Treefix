# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests text v2 invocation."""
with test.mock.patch.object(
    summary_v2, 'text', autospec=True) as mock_text_v2:
    with summary_ops_v2.create_summary_file_writer(
        self.get_temp_dir()).as_default(step=22):
        i = constant_op.constant('lorem ipsum', dtype=dtypes.string)
        tensor = summary_lib.text('text', i)
    # Returns empty string.
self.assertEqual(tensor.numpy(), b'')
self.assertEqual(tensor.dtype, dtypes.string)
mock_text_v2.assert_called_once_with('text', data=i, step=22)
