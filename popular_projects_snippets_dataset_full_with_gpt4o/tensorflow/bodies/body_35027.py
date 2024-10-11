# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
with self.cached_session():
    p = array_ops.placeholder(dtypes.float32, shape=[None, 1])
    dist = bernoulli.Bernoulli(probs=p)
    self.assertEqual(2, len(dist.log_prob(1).eval({p: [[0.5], [0.5]]}).shape))

    dist = bernoulli.Bernoulli(probs=0.5)
    self.assertEqual(2, len(self.evaluate(dist.log_prob([[1], [1]])).shape))

    dist = bernoulli.Bernoulli(probs=0.5)
    self.assertEqual((), dist.log_prob(1).get_shape())
    self.assertEqual((1), dist.log_prob([1]).get_shape())
    self.assertEqual((2, 1), dist.log_prob([[1], [1]]).get_shape())

    dist = bernoulli.Bernoulli(probs=[[0.5], [0.5]])
    self.assertEqual((2, 1), dist.log_prob(1).get_shape())
