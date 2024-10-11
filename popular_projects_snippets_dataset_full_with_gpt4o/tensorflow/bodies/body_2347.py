# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
# Tests that 'rng' does not always return the same value.
# The random-number generator, if working correctly, should produce the
# same output multiple times with low probability.
x = rng(dtype).numpy()
y = rng(dtype).numpy()
self.assertFalse(np.array_equal(x, y))
