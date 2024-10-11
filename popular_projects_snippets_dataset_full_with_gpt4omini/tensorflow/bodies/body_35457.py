# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
with test_util.use_gpu():
    sample_op1, sample_op2 = self._make_ops(1000, seed=1)
    sample1, sample2 = self.evaluate([sample_op1, sample_op2])
    self.assertAllEqual(sample1, sample2)
