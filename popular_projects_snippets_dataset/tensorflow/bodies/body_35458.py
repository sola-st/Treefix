# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
for neg in [True, False]:
    with test_util.use_gpu():
        logits = np.array([[1000.] * 5])
        if neg:
            logits *= -1
        samples = self.evaluate(random_ops.multinomial(logits, 10))
    # Sampled classes should be in-range.
    self.assertTrue((samples >= 0).all())
    self.assertTrue((samples < 5).all())
