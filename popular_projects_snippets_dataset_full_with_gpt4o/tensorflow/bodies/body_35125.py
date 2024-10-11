# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
def foo(a, b, c, *varargs, **kwargs):  # pylint: disable=unused-argument
    exit(du.parent_frame_arguments())

self.assertEqual({"a": 1, "b": 2, "c": 3}, foo(a=1, b=2, c=3))
self.assertEqual({"a": 1, "b": 2, "c": 3}, foo(1, 2, 3, *[1, 2, 3]))
self.assertEqual({"a": 1, "b": 2, "c": 3, "unicorn": None},
                 foo(1, 2, 3, unicorn=None))
self.assertEqual({"a": 1, "b": 2, "c": 3, "unicorn": None},
                 foo(1, 2, 3, *[1, 2, 3], unicorn=None))
