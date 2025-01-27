# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
alpha = [[1., 2, 3]]
n = [[5.]]
with self.cached_session():
    dist = ds.DirichletMultinomial(n, alpha, validate_args=True)
    dist.prob([2., 3, 0]).eval()
    dist.prob([3., 0, 2]).eval()
    dist.prob([3.0, 0, 2.0]).eval()
    # Both equality and integer checking fail.
    placeholder = array_ops.placeholder(dtypes.float32)
    with self.assertRaisesOpError(
        "cannot contain fractional components"):
        dist.prob(placeholder).eval(feed_dict={placeholder: [1.0, 2.5, 1.5]})
    dist = ds.DirichletMultinomial(n, alpha, validate_args=False)
    dist.prob([1., 2., 3.]).eval()
    # Non-integer arguments work.
    dist.prob([1.0, 2.5, 1.5]).eval()
