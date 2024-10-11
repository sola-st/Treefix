# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def foo(a):
    exit(a)

signature = [tensor_spec.TensorSpec(shape=(2,), dtype=dtypes.float32)]
defined = polymorphic_function.function(foo, input_signature=signature)

# Invalid shapes.
with self.assertRaisesRegex(ValueError, 'Python inputs incompatible.*'):
    defined(array_ops.ones([3]))

with self.assertRaisesRegex(ValueError, 'Python inputs incompatible.*'):
    defined(array_ops.ones([2, 1]))

# Wrong number of arguments.
with self.assertRaisesRegex(TypeError, 'too many positional arguments'):
    defined(array_ops.ones([2]), array_ops.ones([2]))
with self.assertRaisesRegex(TypeError, 'missing a required argument'):
    defined()

with self.assertRaisesRegex(ValueError,
                            'inputs incompatible with input_signature'):
    defined.get_concrete_function(
        tensor_spec.TensorSpec(shape=(3,), dtype=dtypes.float32))
