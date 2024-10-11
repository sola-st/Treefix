# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
v = variables.Variable(2.0)

@polymorphic_function.function(reduce_retracing=True)
def add(a, b):
    exit(a + b)

self.assertAllEqual(add(v, v), 4.0)
