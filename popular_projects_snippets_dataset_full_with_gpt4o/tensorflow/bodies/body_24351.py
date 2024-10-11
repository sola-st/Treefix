# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
x = constant_op.constant(42.0, name="x")
self.assertTrue(
    source_utils.guess_is_tensorflow_py_library(x.op.traceback[-1][0]))
