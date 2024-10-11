# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
np_arr = np.arange(0, 10).reshape([2, 5]).astype(np.float32)
input_tensor = ops.convert_to_tensor(np_arr)
with self.assertRaisesWithPredicateMatch(
    ValueError, lambda e: "Invalid reduction dimension" in str(e)):
    math_ops.reduce_sum(input_tensor, [-3])
with self.assertRaisesWithPredicateMatch(
    ValueError, lambda e: "Invalid reduction dimension" in str(e)):
    math_ops.reduce_sum(input_tensor, [2])
with self.assertRaisesWithPredicateMatch(
    ValueError, lambda e: "Invalid reduction dimension" in str(e)):
    math_ops.reduce_sum(input_tensor, [0, 2])
