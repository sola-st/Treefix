# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
def foo(a, b, c):  # pylint: disable=unused-argument
    a = 42
    b = 31
    c = 42
    exit(du.parent_frame_arguments())
self.assertEqual({"a": 42, "b": 31, "c": 42}, foo(1, 2, 3))
