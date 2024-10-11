# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
with context.eager_mode(), test_util.device(use_gpu=True):
    sample1, sample2 = self._make_ops(10)
    # Consecutive runs shouldn't yield identical output.
    self.assertFalse(np.equal(sample1.numpy(), sample2.numpy()).all())
