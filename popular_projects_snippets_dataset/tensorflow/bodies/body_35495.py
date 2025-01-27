# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
rng = stateful_random_ops.Generator.from_seed(12345)
counts = np.array([5, 5, 5, 0, 0, 0], dtype=np.float32)
probs = np.array([0, 1, float("nan"), -10, 10, float("nan")],
                 dtype=np.float32)
expected = np.array([0, 5, float("nan"), 0, 0, 0], dtype=np.float32)
result = rng.binomial(
    shape=[6], counts=counts, probs=probs, dtype=np.float32)
self.assertAllEqual(expected, self.evaluate(result))
