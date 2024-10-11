# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
a = np.isnan(float_type(float("nan")))
self.assertTrue(a)
numpy_assert_allclose(
    np.array([1.0, a]), np.array([1.0, a]), float_type=float_type)

a = np.array(
    [float_type(1.34375),
     float_type(1.4375),
     float_type(float("nan"))],
    dtype=float_type)
b = np.array(
    [float_type(1.3359375),
     float_type(1.4375),
     float_type(float("nan"))],
    dtype=float_type)
numpy_assert_allclose(
    a,
    b,
    rtol=0.1,
    atol=0.1,
    equal_nan=True,
    err_msg="",
    verbose=True,
    float_type=float_type)
