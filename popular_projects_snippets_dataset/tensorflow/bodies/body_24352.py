# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
self.assertFalse(
    source_utils.guess_is_tensorflow_py_library(os.path.normpath(
        "site-packages/tensorflow/python/debug/examples/debug_mnist.py")))
self.assertFalse(
    source_utils.guess_is_tensorflow_py_library(os.path.normpath(
        "site-packages/tensorflow/python/debug/examples/v1/example_v1.py")))
self.assertFalse(
    source_utils.guess_is_tensorflow_py_library(os.path.normpath(
        "site-packages/tensorflow/python/debug/examples/v2/example_v2.py")))
self.assertFalse(
    source_utils.guess_is_tensorflow_py_library(os.path.normpath(
        "site-packages/tensorflow/python/debug/examples/v3/example_v3.py")))
