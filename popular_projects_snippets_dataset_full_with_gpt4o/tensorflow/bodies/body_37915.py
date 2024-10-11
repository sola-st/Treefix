# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.linspace(-5, 20, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args
y = np.linspace(20, -5, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args
self._compareBoth(x, y, np.add, math_ops.add, also_compare_variables=True)
self._compareBoth(x, y, np.subtract, math_ops.subtract)
self._compareBoth(x, y, np.multiply, math_ops.multiply)
self._compareBoth(x, y + 0.1, np.true_divide, math_ops.truediv)
self._compareBoth(x, y + 0.1, np.floor_divide, math_ops.floordiv)
self._compareBoth(x, y, np.add, _ADD)
self._compareBoth(x, y, np.subtract, _SUB)
self._compareBoth(x, y, np.multiply, _MUL)
self._compareBoth(x, y + 0.1, np.true_divide, _TRUEDIV)
self._compareBoth(x, y + 0.1, np.floor_divide, _FLOORDIV)
self._compareBoth(x, y, np.arctan2, math_ops.atan2)
x1 = np.random.randn(5, 6).astype(np.float32)
x2 = np.random.randn(5, 6).astype(np.float32)
# Remove tiny values--atan2 gradients are flaky near the origin.
x1[np.abs(x1) < 0.05] = 0.05 * np.sign(x1[np.abs(x1) < 0.05])
x2[np.abs(x2) < 0.05] = 0.05 * np.sign(x2[np.abs(x2) < 0.05])
self._compareBoth(x1, x2, np.arctan2, math_ops.atan2)
try:
    from scipy import special  # pylint: disable=g-import-not-at-top
    a_pos_small = np.linspace(0.1, 2, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args
    x_pos_small = np.linspace(0.1, 10, 15).reshape(1, 3, 5).astype(np.float32)  # pylint: disable=too-many-function-args
    self._compareBoth(a_pos_small, x_pos_small, special.gammainc,
                      math_ops.igamma)
    self._compareBoth(a_pos_small, x_pos_small, special.gammaincc,
                      math_ops.igammac)
    # Need x > 1
    self._compareBoth(x_pos_small + 1, a_pos_small, special.zeta,
                      math_ops.zeta)
    n_small = np.arange(0, 15).reshape(1, 3, 5).astype(np.float32)
    self._compareBoth(n_small, x_pos_small, special.polygamma,
                      math_ops.polygamma)
except ImportError as e:
    tf_logging.warn("Cannot test special functions: %s" % str(e))
