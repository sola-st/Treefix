# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
with self.cached_session() as sess:
    p = [0.2, 0.6]
    dist = bernoulli.Bernoulli(probs=p)
    n = 1000
    seed = 42
    self.assertAllEqual(
        self.evaluate(dist.sample(n, seed)),
        self.evaluate(dist.sample(n, seed)))
    n = array_ops.placeholder(dtypes.int32)
    sample1, sample2 = sess.run([dist.sample(n, seed), dist.sample(n, seed)],
                                feed_dict={n: 1000})
    self.assertAllEqual(sample1, sample2)
