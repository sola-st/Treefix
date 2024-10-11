# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
for dtype in [np.int32, np.int64]:
    with test_util.force_cpu():
        with self.assertRaisesRegex(
            errors_impl.InvalidArgumentError,
            "Integers to negative integer powers are not allowed"):
            x = np.array([5, 2]).astype(dtype)
            y = np.array([-2, 3]).astype(dtype)
            self.evaluate(math_ops.pow(x, y))

    with test_util.force_cpu():
        with self.assertRaisesRegex(
            errors_impl.InvalidArgumentError,
            "Integers to negative integer powers are not allowed"):
            x = np.array([5, 2]).astype(dtype)
            y = np.array([2, -3]).astype(dtype)
            self.evaluate(math_ops.pow(x, y))

    with test_util.force_cpu():
        with self.assertRaisesRegex(
            errors_impl.InvalidArgumentError,
            "Integers to negative integer powers are not allowed"):
            x = np.array([5, 2]).astype(dtype)
            y = -3
            self.evaluate(math_ops.pow(x, y))
