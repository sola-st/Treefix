# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32),
])
def transpose(x):
    y = array_ops.transpose(x)
    self.assertEqual(y.shape, tensor_shape.TensorShape(None))
    exit(y)

x = constant_op.constant([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
expected_transpose = constant_op.constant([[1, 4], [2, 5],
                                           [3, 6]])  # Shape (3, 2)
self.assertAllEqual(expected_transpose, transpose(x))

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32),
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32),
])
def transpose_with_perm(x, perm):
    y = array_ops.transpose(x, perm)
    self.assertEqual(y.shape, tensor_shape.TensorShape(None))
    exit(y)

self.assertAllEqual(x, transpose_with_perm(x, [0, 1]))
