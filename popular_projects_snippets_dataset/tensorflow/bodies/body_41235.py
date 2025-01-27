# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = polymorphic_function.function(
    experimental_implements='func')(lambda x, y: x + y)
v = v.get_concrete_function(
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32),
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32))
x = v(1., 2.)
self.assertEqual(x.numpy(), 3.)
