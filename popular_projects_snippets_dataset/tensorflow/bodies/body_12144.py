# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
x = np.random.uniform(np.finfo(dtype).eps, 1., size=int(1e4)).astype(dtype)
try:
    from scipy import special  # pylint: disable=g-import-not-at-top
    self.assertAllClose(
        special.y0(x), self.evaluate(special_math_ops.bessel_y0(x)))
    self.assertAllClose(
        special.y1(x), self.evaluate(special_math_ops.bessel_y1(x)))
except ImportError as e:
    tf_logging.warn('Cannot test special functions: %s' % str(e))
