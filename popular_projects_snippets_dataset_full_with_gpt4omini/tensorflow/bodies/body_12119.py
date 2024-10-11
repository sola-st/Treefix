# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
x = np.random.uniform(1., 50., size=int(1e4)).astype(dtype)
try:
    from scipy import special  # pylint: disable=g-import-not-at-top
    self.assertAllClose(
        special.expi(x), self.evaluate(special_math_ops.expint(x)))
except ImportError as e:
    tf_logging.warn('Cannot test special functions: %s' % str(e))
