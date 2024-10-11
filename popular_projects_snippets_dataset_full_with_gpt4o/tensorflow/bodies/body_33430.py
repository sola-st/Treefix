# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = np.zeros((3, 4, 2)).tolist()
op_dimensions = [tensor_shape.Dimension(None) for _ in range(3)]

# Since the leftmost dimension of `x` is equal to the number of blocks, and
# the operators have unknown dimension, the input is ambiguous.
with self.assertRaisesRegex(ValueError, "structure is ambiguous"):
    linear_operator_util.arg_is_blockwise(op_dimensions, x, -2)
