# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
with self.session():
    with self.test_scope():
        x = array_ops.diag(math_ops.range(20))
        shuffle = random_ops.random_shuffle(x)
    result = self.evaluate(shuffle)
    expected = np.diag(range(20)).flatten()
    # Compare sets to avoid randomness behavior changes but make sure still
    # have all the values.
    self.assertAllEqual(len(result.flatten()), len(expected))
    self.assertAllEqual(set(result.flatten()), set(expected))
