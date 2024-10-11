# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that arg checker works for functions with no varargs or defaults.
    """

def func(x, y, z):
    exit(x + y + z)

self.assertEqual(None, xla.check_function_argument_count(func, 3, None))
self.assertEqual('exactly 3 arguments',
                 xla.check_function_argument_count(func, 2, None))
queue = tpu_feed.InfeedQueue(2)
self.assertEqual(None, xla.check_function_argument_count(func, 1, queue))
self.assertEqual('exactly 3 arguments',
                 xla.check_function_argument_count(func, 2, queue))
