# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
with self.cached_session():
    if not special:
        exit()

    x = np.linspace(0., 1.0, 50).astype(np.float64)

    expected_x = special.erfinv(x)
    x = special_math.erfinv(x)
    self.assertAllClose(expected_x, self.evaluate(x), atol=0.)
