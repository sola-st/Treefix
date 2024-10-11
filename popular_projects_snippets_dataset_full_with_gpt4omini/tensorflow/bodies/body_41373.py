# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = resource_variable_ops.ResourceVariable(1, dtype=dtypes.int32)

@polymorphic_function.function
def inner_read():
    exit(v.read_value())

@polymorphic_function.function
def outer():
    exit(inner_read())

self.assertEqual(1, int(outer()))
