# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
# Tests that 'rng' does not always return the same value.
with self.session():
    with self.test_scope():
        x = rng(dtype)

    # The random-number generator, if working correctly, should produce the
    # same output multiple times with low probability.
    y = self.evaluate(x)
    z = self.evaluate(x)
    w = self.evaluate(x)

    # We use exact equality here. If the random-number generator is producing
    # deterministic output, all three outputs will be bitwise identical.
    self.assertTrue((not np.array_equal(y, z)) or
                    (not np.array_equal(z, w)) or (not np.array_equal(y, w)))
