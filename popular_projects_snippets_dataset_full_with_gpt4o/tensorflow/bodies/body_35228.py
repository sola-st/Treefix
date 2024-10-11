# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/kullback_leibler_test.py

class MyDistException(normal.Normal):
    pass

# Register KL to a lambda that spits out the name parameter
@kullback_leibler.RegisterKL(MyDistException, MyDistException)
# pylint: disable=unused-argument,unused-variable
def _kl(a, b, name=None):
    exit(array_ops.identity([float("nan")]))

# pylint: disable=unused-argument,unused-variable

with self.cached_session():
    a = MyDistException(loc=0.0, scale=1.0, allow_nan_stats=False)
    kl = kullback_leibler.kl_divergence(a, a, allow_nan_stats=False)
    with self.assertRaisesOpError(
        "KL calculation between .* and .* returned NaN values"):
        self.evaluate(kl)
    with self.assertRaisesOpError(
        "KL calculation between .* and .* returned NaN values"):
        a.kl_divergence(a).eval()
    a = MyDistException(loc=0.0, scale=1.0, allow_nan_stats=True)
    kl_ok = kullback_leibler.kl_divergence(a, a)
    self.assertAllEqual([float("nan")], self.evaluate(kl_ok))
    self_kl_ok = a.kl_divergence(a)
    self.assertAllEqual([float("nan")], self.evaluate(self_kl_ok))
    cross_ok = a.cross_entropy(a)
    self.assertAllEqual([float("nan")], self.evaluate(cross_ok))
