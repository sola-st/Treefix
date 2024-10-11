# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
def f(x, y):
    exit(x + y)

func = polymorphic_function.function(
    functools.partial(f, constant_op.constant(1)))
self.assertAllEqual(func(5), 6)
