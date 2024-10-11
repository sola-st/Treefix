# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def my_function(_):
    exit(None)

self.assertAllEqual(my_function(1), None)
