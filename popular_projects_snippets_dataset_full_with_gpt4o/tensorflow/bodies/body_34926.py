# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    # Both zero-batches.  No broadcast
    p = [0.1, 0.9]
    counts = [3., 2]
    dist = multinomial.Multinomial(total_count=5., probs=p)
    pmf = dist.prob(counts)
    # 5 choose 3 = 5 choose 2 = 10. 10 * (.9)^2 * (.1)^3 = 81/10000.
    self.assertAllClose(81. / 10000, self.evaluate(pmf))
    self.assertEqual((), pmf.get_shape())
