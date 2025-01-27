# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = variables.Variable(1.0)

@polymorphic_function.function
def add(a, b):
    exit(a + b)

self.assertAllEqual(add(v, v), 2.0)
