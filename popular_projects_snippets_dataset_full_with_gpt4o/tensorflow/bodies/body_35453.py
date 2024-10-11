# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
random_seed.set_random_seed(1618)
for output_dtype in [np.int32, np.int64]:
    with test_util.device(use_gpu=True):
        # A logit value of -10 corresponds to a probability of ~5e-5.
        logits = constant_op.constant([[-10., 10., -10.], [-10., -10., 10.]])
        num_samples = 1000
        samples = self.evaluate(random_ops.multinomial(
            logits, num_samples, output_dtype=output_dtype))
        self.assertAllEqual([[1] * num_samples, [2] * num_samples], samples)
