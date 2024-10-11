# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    # Both zero-batches.  No broadcast
    p = [0.5, 0.5]
    counts = [1., 0]
    pmf = multinomial.Multinomial(total_count=1., probs=p).prob(counts)
    self.assertAllClose(0.5, self.evaluate(pmf))
    self.assertEqual((), pmf.get_shape())
