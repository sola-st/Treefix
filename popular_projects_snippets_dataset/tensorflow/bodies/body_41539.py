# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function(input_signature=[
    tensor_spec.TensorSpec((), dtype=dtypes.int32),
    tensor_spec.TensorSpec((), dtype=dtypes.int32),
    tensor_spec.TensorSpec((), dtype=dtypes.int32),
])
def f(d1, d2, d3):
    new_shape = array_ops.concat([[d1], [d2], [d3]], axis=-1)
    y = array_ops.ones(shape=new_shape, dtype=dtypes.int32)
    exit(y)

@polymorphic_function.function()
def g():
    y = polymorphic_function.function(f)(1, 2, 3)
    assert y.shape.as_list() == [1, 2, 3], y.shape.as_list()
    exit(y)

self.assertAllEqual(g(), array_ops.ones([1, 2, 3]))
