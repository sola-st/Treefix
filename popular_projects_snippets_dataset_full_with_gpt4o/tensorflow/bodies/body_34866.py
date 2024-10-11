# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
alpha = [[1., 2, 3]]
n = [[5.]]
with self.cached_session():
    dist = ds.DirichletMultinomial(n, alpha, validate_args=True)
    dist.prob([2., 3, 0]).eval()
    dist.prob([3., 0, 2]).eval()
    with self.assertRaisesOpError("must be non-negative"):
        dist.prob([-1., 4, 2]).eval()
    with self.assertRaisesOpError(
        "last-dimension must sum to `self.total_count`"):
        dist.prob([3., 3, 0]).eval()
