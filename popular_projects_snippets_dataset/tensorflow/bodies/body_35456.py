# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
with test_util.use_gpu():
    sample_op1, sample_op2 = self._make_ops(32)
    sample1, sample2 = self.evaluate([sample_op1, sample_op2])
    # We expect sample1 and sample2 to be independent.
    # 1 in 2^32 chance of this assertion failing.
    self.assertFalse(np.equal(sample1, sample2).all())
