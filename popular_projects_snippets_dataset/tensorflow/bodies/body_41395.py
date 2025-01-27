# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def foo(a, b):
    del a
    del b

# Signatures must consist exclusively of `TensorSpec` objects.
signature = [(2, 3), tensor_spec.TensorSpec([2, 3], dtypes.float32)]
with self.assertRaisesRegex(TypeError, 'input_signature.*nested sequence'):
    polymorphic_function.function(foo, input_signature=signature)
