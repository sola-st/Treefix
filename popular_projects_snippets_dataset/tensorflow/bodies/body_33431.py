# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = np.zeros((2, 3, 4, 6)).tolist()
op_dimension_values = [4, 3]
op_dimensions = [tensor_shape.Dimension(v) for v in op_dimension_values]

# The dimensions of the two operator-blocks sum to 7. `x` is a
# two-element list; if interpreted blockwise, its corresponding dimensions
# sum to 12 (=6*2). If not interpreted blockwise, its corresponding
# dimension is 6. This is a mismatch.
with self.assertRaisesRegex(ValueError, "dimension does not match"):
    linear_operator_util.arg_is_blockwise(op_dimensions, x, -1)
