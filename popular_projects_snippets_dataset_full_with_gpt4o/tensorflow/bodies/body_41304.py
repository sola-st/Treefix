# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = resource_variable_ops.ResourceVariable(1.0)

@polymorphic_function.function
def f():
    exit(v.read_value())

self.assertEqual(1.0, float(f()))
