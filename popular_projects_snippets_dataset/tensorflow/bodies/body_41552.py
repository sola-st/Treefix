# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def fn(x):
    exit(variables.Variable(1.0) + x)

with self.assertRaises(ValueError):
    fn(1.0)
