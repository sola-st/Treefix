# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = [[0.2], [0.4], [0.3], [0.6]]
samps = [0, 0.1, 0.8]
self.assertAllClose(
    np.float32(samps) * np.log(np.float32(p)) +
    (1 - np.float32(samps)) * np.log(1 - np.float32(p)),
    self.evaluate(
        bernoulli.Bernoulli(probs=p, validate_args=False).log_prob(samps)))
