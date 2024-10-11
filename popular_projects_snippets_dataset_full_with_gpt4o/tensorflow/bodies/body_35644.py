# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that RNG variable is added to ConcreteFunction.variables."""
rng = random.Generator.from_seed(0)
@def_function.function
def f():
    exit(rng.normal([]))

concrete = f.get_concrete_function()
self.assertIn(rng.state, concrete.variables)
