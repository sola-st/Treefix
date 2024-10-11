# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests creating generator with a variable.
    """
alg = random.RNG_ALG_PHILOX
state = [1, 2, 3]
var = variables.Variable(state, dtype=random.STATE_TYPE)
g = random.Generator(state=state, alg=alg)
g_var = random.Generator(state=var, alg=alg)
shape = [2, 3]
g.normal(shape)
g_var.normal(shape)
self.assertAllEqual(g.state.read_value(), var.read_value())
