# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
filepath = '/filesystem/path/tensorflow/python/tpu/example_test.runfiles/tensorflow/python/tpu/example_test'  # pylint: disable=line-too-long
self.assertEqual(
    tpu_test_wrapper.calculate_parent_python_path(filepath),
    'tensorflow.python.tpu')
