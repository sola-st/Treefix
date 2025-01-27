# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
with self.session():
    with self.test_scope():
        x = math_ops.range(1 << 16)
        shuffle = random_ops.random_shuffle(x)
    result = self.evaluate(shuffle)
    expected = range(1 << 16)
    # Compare sets to avoid randomness behavior changes but make sure still
    # have all the values.
    self.assertAllEqual(set(result), set(expected))
