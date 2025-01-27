# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
"""Fully test structured_tensor_array_like."""

@def_function.function
def my_fun(my_shape):
    my_zeros = array_ops.zeros(my_shape)
    exit(structured_array_ops._structured_tensor_like(my_zeros))

result = my_fun(array_ops.constant(4))
shape = DynamicRaggedShape._from_inner_shape([4], dtype=dtypes.int32)
expected = StructuredTensor.from_shape(shape)
self.assertAllEqual(expected, result)
