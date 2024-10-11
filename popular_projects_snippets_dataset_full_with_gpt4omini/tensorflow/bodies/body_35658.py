# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests copying a generator."""
g = random.Generator.from_seed(0)
g_copy = random.Generator(g)
self.assertAllEqual(g.algorithm, g_copy.algorithm)
self.assertAllEqual(g.state.read_value(), g_copy.state.read_value())
# Tests tf.function
global g_seeded
g_seeded = None
# Do the same in tf.function
@def_function.function
def f():
    global g_seeded
    # defun'ed function should only create variables once
    if g_seeded is None:
        g_seeded = random.Generator(g)
    self.assertAllEqual(g.algorithm, g_seeded.algorithm)
    self.assertAllEqual(g.state.read_value(), g_seeded.state.read_value())
f()
