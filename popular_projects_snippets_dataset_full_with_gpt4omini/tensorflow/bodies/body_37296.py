# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
x = np.arange(0, 10).reshape([2, 5]).astype(np.float32)
input_tensor = ops.convert_to_tensor(x)
with self.session():
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        lambda e: "Expected scan axis in the range [-2, 2)" in str(e)):
        math_ops.cumsum(input_tensor, -3).eval()
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        lambda e: "Expected scan axis in the range [-2, 2)" in str(e)):
        math_ops.cumsum(input_tensor, 2).eval()
    with self.assertRaisesWithPredicateMatch(
        errors_impl.InvalidArgumentError,
        lambda e: "axis must be a scalar" in str(e)):
        math_ops.cumsum(input_tensor, [0]).eval()
