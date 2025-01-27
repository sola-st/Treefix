# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x):
    exit({'name': x + 1})

self.assertAllEqual(f(constant_op.constant(1.0))['name'], 2.0)
