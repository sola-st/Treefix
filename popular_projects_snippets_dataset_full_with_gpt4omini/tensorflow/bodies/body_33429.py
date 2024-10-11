# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = np.zeros((2, 3, 4, 6))
x_tensor = ops.convert_to_tensor(x)
x_placeholder = array_ops.placeholder_with_default(x, shape=None)
x_list = x.tolist()

# For known and matching operator dimensions, interpret all as non-blockwise
op_dimension_values = [2, 1, 3]
op_dimensions = [tensor_shape.Dimension(d) for d in op_dimension_values]
for inputs in [x, x_tensor, x_placeholder, x_list]:
    self.assertFalse(linear_operator_util.arg_is_blockwise(
        op_dimensions, inputs, -1))

# The input is still interpreted as non-blockwise for unknown operator
# dimensions (`x_list` has an outermost dimension that does not matcn the
# number of blocks, and the other inputs are not iterables).
unknown_op_dimensions = [
    tensor_shape.Dimension(None) for _ in op_dimension_values]
for inputs in [x, x_tensor, x_placeholder, x_list]:
    self.assertFalse(linear_operator_util.arg_is_blockwise(
        unknown_op_dimensions, inputs, -1))
