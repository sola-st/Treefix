# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
np.testing.assert_equal(
    np.arange(100, dtype=np.float32).astype(float_type),
    np.arange(100, dtype=float_type))
np.testing.assert_equal(
    np.arange(-8, 8, 1, dtype=np.float32).astype(float_type),
    np.arange(-8, 8, 1, dtype=float_type))
np.testing.assert_equal(
    np.arange(-0., -2., -0.25, dtype=np.float32).astype(float_type),
    np.arange(-0., -2., -0.25, dtype=float_type))
np.testing.assert_equal(
    np.arange(-16., 16., 2., dtype=np.float32).astype(float_type),
    np.arange(-16., 16., 2., dtype=float_type))
