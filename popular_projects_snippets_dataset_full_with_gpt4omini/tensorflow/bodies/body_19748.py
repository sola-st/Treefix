# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
filepath = '/bad/path'
with self.assertRaisesWithLiteralMatch(
    ValueError,
    'Filepath "/bad/path" does not contain repo root "tensorflow/python"'):
    tpu_test_wrapper.calculate_parent_python_path(filepath)
