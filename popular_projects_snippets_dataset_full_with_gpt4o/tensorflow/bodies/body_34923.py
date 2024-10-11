# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
p = [[0.1, 0.2, 0.7]]
n = [[5.]]
with self.cached_session():
    dist = multinomial.Multinomial(total_count=n, probs=p, validate_args=True)
    dist.prob([2., 3, 0]).eval()
    dist.prob([3., 0, 2]).eval()
    with self.assertRaisesOpError("must be non-negative"):
        dist.prob([-1., 4, 2]).eval()
    with self.assertRaisesOpError("counts must sum to `self.total_count`"):
        dist.prob([3., 3, 0]).eval()
