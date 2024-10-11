# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function(input_signature=[
    tensor_spec.TensorSpec((None, None), dtype=dtypes.int32),
    tensor_spec.TensorSpec((), dtype=dtypes.int32),
])
def f(x, s):
    old_shape = array_ops.shape(x)
    new_shape = array_ops.stack([old_shape[0], s], axis=0)
    y = array_ops.ones(shape=new_shape, dtype=dtypes.int32)
    exit(y)

@polymorphic_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=(3, 6), dtype=dtypes.int32)
])
def g(x):
    y = f(x, s=5)
    assert y.shape.as_list() == [3, 5], y.shape.as_list()
    exit(y)

self.assertAllEqual(
    g(array_ops.zeros([3, 6], dtype=dtypes.int32)), array_ops.ones([3, 5]))
