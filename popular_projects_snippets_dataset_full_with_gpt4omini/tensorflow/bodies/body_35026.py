# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
with self.cached_session():
    p = array_ops.placeholder(dtypes.float32)
    dist = bernoulli.Bernoulli(probs=p)
    self.assertAllClose(np.log(0.5), dist.log_prob(1).eval({p: 0.5}))
    self.assertAllClose(
        np.log([0.5, 0.5, 0.5]), dist.log_prob([1, 1, 1]).eval({
            p: 0.5
        }))
    self.assertAllClose(
        np.log([0.5, 0.5, 0.5]), dist.log_prob(1).eval({
            p: [0.5, 0.5, 0.5]
        }))
