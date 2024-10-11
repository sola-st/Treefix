# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
x = np.random.uniform(-1., 1., size=int(1e4)).astype(dtype)
try:
    from scipy import special  # pylint: disable=g-import-not-at-top
    self.assertAllClose(
        special.i0(x), self.evaluate(special_math_ops.bessel_i0(x)))
    self.assertAllClose(
        special.i1(x), self.evaluate(special_math_ops.bessel_i1(x)))
    self.assertAllClose(
        special.i0e(x), self.evaluate(special_math_ops.bessel_i0e(x)))
    self.assertAllClose(
        special.i1e(x), self.evaluate(special_math_ops.bessel_i1e(x)))
except ImportError as e:
    tf_logging.warn('Cannot test special functions: %s' % str(e))
