# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
for func in [
    math_ops.add, math_ops.subtract, math_ops.multiply, math_ops.div, _ADD,
    _SUB, _MUL, _TRUEDIV, _FLOORDIV
]:
    with self.assertRaisesWithPredicateMatch(
        ValueError, lambda e: "Dimensions must" in str(e)):
        func(
            ops.convert_to_tensor([10.0, 20.0, 30.0]),
            ops.convert_to_tensor([[40.0, 50.0], [60.0, 70.0]]))
