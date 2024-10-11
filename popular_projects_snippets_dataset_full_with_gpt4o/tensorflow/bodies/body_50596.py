# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests histogram v2 invocation."""
with test.mock.patch.object(
    summary_v2, 'histogram', autospec=True) as mock_histogram_v2:
    with summary_ops_v2.create_summary_file_writer(
        self.get_temp_dir()).as_default(step=3):
        i = array_ops.ones((1024,))
        tensor = summary_lib.histogram('histogram', i, family='family')
    # Returns empty string.
self.assertEqual(tensor.numpy(), b'')
self.assertEqual(tensor.dtype, dtypes.string)
mock_histogram_v2.assert_called_once_with(
    'family/family/histogram', data=i, step=3)
