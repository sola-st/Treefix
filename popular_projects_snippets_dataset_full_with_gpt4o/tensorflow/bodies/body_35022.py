# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
with self.cached_session():
    p = array_ops.placeholder(dtype=dtypes.float32)
    dist = bernoulli.Bernoulli(probs=p)
    event1 = [1, 0, 1]
    event2 = [[1, 0, 1]]
    self.assertAllClose(
        dist.prob(event1).eval({
            p: [0.2, 0.3, 0.4]
        }), [0.2, 0.7, 0.4])
    self.assertAllClose(
        dist.prob(event2).eval({
            p: [0.2, 0.3, 0.4]
        }), [[0.2, 0.7, 0.4]])
