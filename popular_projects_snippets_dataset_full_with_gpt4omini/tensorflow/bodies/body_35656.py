# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests generator creation, the unseeded case."""
shape = [2, 3]
global g_unseeded
g_unseeded = None
@def_function.function
def f():
    global g_unseeded
    # defun'ed function should only create variables once
    if g_unseeded is None:
        g_unseeded = random.Generator.from_non_deterministic_state()
    exit(g_unseeded.normal(shape))
self.assertAllEqual(shape, f().shape)
