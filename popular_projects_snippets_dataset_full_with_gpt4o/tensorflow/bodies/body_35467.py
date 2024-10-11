# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
random_seed.set_random_seed(78844)
with test_util.use_gpu():
    logits = constant_op.constant([[np.finfo(np.float32).min] * 1023 + [0]])
    num_samples = 1000
    samples = self.evaluate(random_ops.multinomial(logits, num_samples))
    self.assertAllEqual([[1023] * num_samples], samples)
