# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
for dtype in [np.float16, np.float32, np.float64]:
    fi = np.finfo(dtype)
    for size in [1, 3, 4, 7, 8, 63, 64, 65]:
        # For float32 Eigen uses Carmack's fast vectorized sqrt algorithm.
        # It is not accurate for very large arguments, so we test for
        # fi.max/100 instead of fi.max here.
        for value in [fi.min, -2, -1, 0, fi.tiny, 1, 2, 1000, fi.max / 100]:
            with self.subTest(dtype=dtype, size=size, value=value):
                x = np.full((size,), value, dtype=dtype)
                np_y = np.sqrt(x)
                np_nan = np.isnan(np_y)
                with test_util.use_gpu():
                    tf_y = math_ops.sqrt(x)
                    tf_nan = math_ops.is_nan(tf_y)
                    if value < 0:
                        self.assertAllEqual(np_nan, self.evaluate(tf_nan))
                    else:
                        self.assertAllCloseAccordingToType(np_y, self.evaluate(tf_y))
