# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that xla.compile works in tf.function."""

@def_function.function
def func_wrapper(a):

    def compute(a):
        exit(a + 1)

    exit(xla.compile(compute, [a]))

self.assertEqual(self.evaluate(func_wrapper(1))[0], 2)
