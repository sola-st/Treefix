# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for dtype in [
    float_type, np.float16, np.float32, np.float64, np.longdouble
]:
    with self.subTest(dtype.__name__):
        for v in FLOAT_VALUES[float_type]:
            np.testing.assert_equal(dtype(v), dtype(float_type(dtype(v))))
            np.testing.assert_equal(dtype(v), dtype(float_type(dtype(v))))
            np.testing.assert_equal(
                dtype(v), dtype(float_type(np.array(v, dtype))))
        if dtype != float_type:
            np.testing.assert_equal(
                np.array(FLOAT_VALUES[float_type], dtype),
                float_type(np.array(FLOAT_VALUES[float_type],
                                    dtype)).astype(dtype))
