# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests audio v2 invocation."""
with test.mock.patch.object(
    summary_v2, 'audio', autospec=True) as mock_audio_v2:
    with summary_ops_v2.create_summary_file_writer(
        self.get_temp_dir()).as_default(step=10):
        i = array_ops.ones((5, 3, 4))
        with ops.name_scope_v2('dolphin'):
            tensor = summary_lib.audio('wave', i, 0.2, max_outputs=3)
    # Returns empty string.
self.assertEqual(tensor.numpy(), b'')
self.assertEqual(tensor.dtype, dtypes.string)
mock_audio_v2.assert_called_once_with(
    'dolphin/wave', data=i, sample_rate=0.2, step=10, max_outputs=3)
