# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
"""Use Anderson-Darling test to test distribution appears normal."""
with self.session() as sess, self.test_scope():
    seed_t = array_ops.placeholder(dtypes.int32, shape=[2])
    n = 1000
    x = stateless.stateless_random_normal(shape=[n], seed=seed_t, dtype=dtype)
    y = sess.run(x, {seed_t: seed})
    # The constant 2.492 is the 5% critical value for the Anderson-Darling
    # test where the mean and variance are known. This test is probabilistic
    # so to avoid flakiness the seed is fixed.
    self.assertLess(random_test_util.anderson_darling(y.astype(float)), 2.492)
