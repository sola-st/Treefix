# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for dtype in [np.float16, np.float32, np.float64, np.longdouble]:
    for f in FLOAT_VALUES[float_type]:
        np.testing.assert_equal(dtype(f), dtype(float_type(dtype(f))))
        np.testing.assert_equal(float(dtype(f)), float(float_type(dtype(f))))
        np.testing.assert_equal(dtype(f), dtype(float_type(np.array(f, dtype))))

    np.testing.assert_equal(
        dtype(np.array(FLOAT_VALUES[float_type], float_type)),
        np.array(FLOAT_VALUES[float_type], dtype))
