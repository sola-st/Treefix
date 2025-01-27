# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
def foo():
    exit(du.parent_frame_arguments())

self.assertEqual({}, foo())
