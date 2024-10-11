# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
p = [[0.1, 0.2, 0.7]]
n = [[5.]]
with self.cached_session():
    # No errors with integer n.
    multinom = multinomial.Multinomial(
        total_count=n, probs=p, validate_args=True)
    multinom.prob([2., 1, 2]).eval()
    multinom.prob([3., 0, 2]).eval()
    # Counts don't sum to n.
    with self.assertRaisesOpError("counts must sum to `self.total_count`"):
        multinom.prob([2., 3, 2]).eval()
    # Counts are non-integers.
    x = array_ops.placeholder(dtypes.float32)
    with self.assertRaisesOpError(
        "cannot contain fractional components."):
        multinom.prob(x).eval(feed_dict={x: [1.0, 2.5, 1.5]})

    multinom = multinomial.Multinomial(
        total_count=n, probs=p, validate_args=False)
    multinom.prob([1., 2., 2.]).eval()
    # Non-integer arguments work.
    multinom.prob([1.0, 2.5, 1.5]).eval()
