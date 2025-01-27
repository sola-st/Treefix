# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f(x):
    exit(x + 1)

@polymorphic_function.function
def g(x):
    x = f(x)
    self.assertEqual(x.shape.as_list(), [])
    exit(None)

g(constant_op.constant(1.0))
