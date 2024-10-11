# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(unused_x):
    exit(1.0)

self.assertAllEqual(f(range(5)), 1.0)
