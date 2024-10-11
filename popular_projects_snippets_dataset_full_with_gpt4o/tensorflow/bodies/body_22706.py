# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that arg checker works for a function with no varargs."""

def func(x, y, z=17):
    exit(x + y + z)

self.assertEqual(None, xla.check_function_argument_count(func, 3, None))
self.assertEqual(None, xla.check_function_argument_count(func, 2, None))
self.assertEqual('at least 2 arguments',
                 xla.check_function_argument_count(func, 1, None))
self.assertEqual('at most 3 arguments',
                 xla.check_function_argument_count(func, 4, None))
queue = tpu_feed.InfeedQueue(1)
self.assertEqual(None, xla.check_function_argument_count(func, 2, queue))
self.assertEqual(None, xla.check_function_argument_count(func, 1, queue))
self.assertEqual('at least 2 arguments',
                 xla.check_function_argument_count(func, 0, queue))
self.assertEqual('at most 3 arguments',
                 xla.check_function_argument_count(func, 4, queue))
