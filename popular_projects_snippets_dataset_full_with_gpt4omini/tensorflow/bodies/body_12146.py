# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
x = np.random.uniform(1., 30., size=int(1e4)).astype(dtype)
try:
    from scipy import special  # pylint: disable=g-import-not-at-top
    self.assertAllClose(
        special.j0(x), self.evaluate(special_math_ops.bessel_j0(x)))
    self.assertAllClose(
        special.j1(x), self.evaluate(special_math_ops.bessel_j1(x)))
except ImportError as e:
    tf_logging.warn('Cannot test special functions: %s' % str(e))
