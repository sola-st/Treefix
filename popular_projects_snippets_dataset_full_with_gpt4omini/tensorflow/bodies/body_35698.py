# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that RNG can be used as tf.function's argument.
    """
shape = [2, 3]
@def_function.function
def f(gen):
    exit(gen.normal(shape))
g1 = random.Generator.from_seed(1)
g2 = random.Generator.from_seed(1)
res1 = f(g1)
res2 = g2.normal(shape)
self.assertAllEqual(res1, res2)
self.assertAllEqual(g1.state.read_value(), g2.state.read_value())
