# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def f(v):
    v.assign_add(1)

signature = [
    resource_variable_ops.VariableSpec(shape=[], dtype=dtypes.int32)
]
with self.assertRaisesRegex(TypeError,
                            "input_signature doesn't support VariableSpec"):
    polymorphic_function.function(f, input_signature=signature)
