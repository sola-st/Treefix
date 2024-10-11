# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests audio v2 invocation with 2-D tensor input."""
with test.mock.patch.object(
    summary_v2, 'audio', autospec=True) as mock_audio_v2:
    with summary_ops_v2.create_summary_file_writer(
        self.get_temp_dir()).as_default(step=11):
        input_2d = array_ops.ones((5, 3))
        tensor = summary_lib.audio('wave', input_2d, 0.2, max_outputs=3)

    # Returns empty string.
self.assertEqual(tensor.numpy(), b'')
self.assertEqual(tensor.dtype, dtypes.string)

mock_audio_v2.assert_called_once_with(
    'wave', data=test.mock.ANY, sample_rate=0.2, step=11, max_outputs=3)
input_3d = array_ops.ones((5, 3, 1))  # 3-D input tensor
self.assertAllEqual(mock_audio_v2.call_args[1]['data'], input_3d)
