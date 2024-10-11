# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
x = np.random.uniform(0., 1., size=int(1e4)).astype(dtype)
try:
    from scipy import special  # pylint: disable=g-import-not-at-top
    self.assertAllClose(
        special.fresnel(x)[1], self.evaluate(special_math_ops.fresnel_cos(x)))
except ImportError as e:
    tf_logging.warn('Cannot test special functions: %s' % str(e))
