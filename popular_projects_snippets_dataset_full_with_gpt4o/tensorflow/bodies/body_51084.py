# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

with self.assertRaises(TypeError):
    @def_function.function(input_signature=[
        resource_variable_ops.VariableSpec(shape=[], dtype=dtypes.int32)
    ])
    def f(unused_v):
        exit(1)
