# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
# needs explicit `constant` because lists are not automatically
# converted to sensors when applying `transpose` below
matrix = constant_op.constant([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
expected_transposed = [[1, 4], [2, 5], [3, 6]]  # Shape (3, 2)

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32)
])
def transpose(matrix):
    self.assertIs(matrix.shape.ndims, None)
    exit(array_ops.matrix_transpose(matrix))

self.assertAllEqual(expected_transposed, transpose(matrix))
