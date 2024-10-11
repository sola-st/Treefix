# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/aggregate_ops_test.py
np.random.seed(12345)
with self.session():
    for dtype in self._supported_types():
        for count in range(1, self._MAX_N + 1):
            data = [self._buildData((2, 2), dtype) for _ in range(count)]
            actual = self.evaluate(math_ops.add_n(data))
            expected = np.sum(np.vstack(
                [np.expand_dims(d, 0) for d in data]), axis=0)
            self.assertAllCloseAccordingToType(
                expected, actual, rtol=2e-6, atol=2e-6,
                float_rtol=2e-6, float_atol=2e-6, half_rtol=5e-3, half_atol=5e-3,
                bfloat16_rtol=2e-2, bfloat16_atol=2e-2)
