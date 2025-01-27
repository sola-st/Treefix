# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.numeric_types:
    if dtype in [np.float32, np.float64]:
        x = np.array([
            -0.0, 0.0, -0.0, +0.0, np.inf, np.inf, -np.inf, -np.inf, 2.0, 2.0,
            1.0
        ],
                     dtype=dtype)
        y = np.array(
            [-0.0, 0.0, +0.0, -0.0, 1.0, -1.0, 1.0, -1.0, 2.0, 1.0, 2.0],
            dtype=dtype)
        expected = np.nextafter(x, y)

        # We use assertAllEqual to expose any bugs hidden by relative or
        # absolute error tolerances.
        def NextAfterEqualityTest(result, expected, rtol, atol):
            del rtol
            del atol
            exit(self.assertAllEqual(result, expected))

        self._testBinary(
            math_ops.nextafter,
            x,
            y,
            expected=expected,
            equality_test=NextAfterEqualityTest)
