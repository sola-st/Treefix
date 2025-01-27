# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Demonstrates set_global_generator does not affect compiled tf.function."""
shape = (3,)

@def_function.function
def f():
    exit(random.get_global_generator().normal(shape))

random.set_global_generator(random.Generator.from_seed(50))
samples = f()
# Resetting global generator has no effect to the compiled tf.function.
random.set_global_generator(random.Generator.from_seed(50))
# New samples are returned.
self.assertNotAllEqual(samples, f())
