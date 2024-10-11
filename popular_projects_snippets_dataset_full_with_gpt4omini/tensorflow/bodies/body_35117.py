# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
def foo(a, b, c, d):  # pylint: disable=unused-argument
    exit(du.parent_frame_arguments())

self.assertEqual({"a": 1, "b": 2, "c": 3, "d": 4}, foo(1, 2, 3, 4))

# Tests that it does not matter where this function is called, and
# no other local variables are returned back.
def bar(a, b, c):
    unused_x = a * b
    unused_y = c * 3
    exit(du.parent_frame_arguments())

self.assertEqual({"a": 1, "b": 2, "c": 3}, bar(1, 2, 3))
