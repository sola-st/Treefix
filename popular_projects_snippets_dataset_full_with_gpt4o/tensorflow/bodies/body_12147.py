# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
x = np.random.uniform(1., 30., size=int(1e4)).astype(dtype)
try:
    from scipy import special  # pylint: disable=g-import-not-at-top
    self.assertAllClose(
        special.k0(x), self.evaluate(special_math_ops.bessel_k0(x)))
    self.assertAllClose(
        special.k0e(x), self.evaluate(special_math_ops.bessel_k0e(x)))
    self.assertAllClose(
        special.k1(x), self.evaluate(special_math_ops.bessel_k1(x)))
    self.assertAllClose(
        special.k1e(x), self.evaluate(special_math_ops.bessel_k1e(x)))
except ImportError as e:
    tf_logging.warn('Cannot test special functions: %s' % str(e))
