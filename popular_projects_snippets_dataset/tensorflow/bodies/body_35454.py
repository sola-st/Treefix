# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
with test_util.use_gpu():
    sample_op1, _ = self._make_ops(10)
    # Consecutive runs shouldn't yield identical output.
    sample1a = self.evaluate(sample_op1)
    sample1b = self.evaluate(sample_op1)
    self.assertFalse(np.equal(sample1a, sample1b).all())
