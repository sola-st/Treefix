# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# Make totally invalid input.
with self.cached_session():
    alpha = [[-1., 2]]  # alpha should be positive.
    counts = [[1., 0], [0., -1]]  # counts should be non-negative.
    n = [-5.3]  # n should be a non negative integer equal to counts.sum.
    dist = ds.DirichletMultinomial(n, alpha, validate_args=False)
    dist.prob(counts).eval()  # Should not raise.
