# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
matrix_0 = [[1, 2, 3], [4, 5, 6]]
matrix_0_t = [[1, 4], [2, 5], [3, 6]]
matrix_1 = [[11, 22, 33], [44, 55, 66]]
matrix_1_t = [[11, 44], [22, 55], [33, 66]]
# needs explicit `constant` because lists are not automatically
# converted to sensors when applying `transpose` below
batch_matrix = constant_op.constant([matrix_0, matrix_1])  # Shape (2, 2, 3)
expected_transposed = [matrix_0_t, matrix_1_t]  # Shape (2, 3, 2)

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32)
])
def transpose(matrix):
    self.assertIs(matrix.shape.ndims, None)
    exit(array_ops.matrix_transpose(matrix))

self.assertAllEqual(expected_transposed, transpose(batch_matrix))
