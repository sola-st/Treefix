# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function(input_signature=[
    tensor_spec.TensorSpec((None, None), dtype=dtypes.int32),
    tensor_spec.TensorSpec((), dtype=dtypes.int32),
])
def f(x, s):
    s0, _ = array_ops.unstack(array_ops.shape(x), axis=0)
    new_shape = array_ops.stack([s0, s], axis=0)
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
