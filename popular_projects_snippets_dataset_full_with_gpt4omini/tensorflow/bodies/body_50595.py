# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests image v2 invocation."""
with test.mock.patch.object(
    summary_v2, 'image', autospec=True) as mock_image_v2:
    with summary_ops_v2.create_summary_file_writer(
        self.get_temp_dir()).as_default(step=2):
        i = array_ops.ones((5, 4, 4, 3))
        with ops.name_scope_v2('outer'):
            tensor = summary_lib.image('image', i, max_outputs=3, family='family')
    # Returns empty string.
self.assertEqual(tensor.numpy(), b'')
self.assertEqual(tensor.dtype, dtypes.string)
mock_image_v2.assert_called_once_with(
    'family/outer/family/image', data=i, step=2, max_outputs=3)
