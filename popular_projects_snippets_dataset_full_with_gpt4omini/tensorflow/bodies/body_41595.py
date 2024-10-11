# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
def f(x, y):
    exit(x + y)

func = polymorphic_function.function(
    functools.partial(f, x=array_ops.zeros([1]), y=array_ops.zeros([1])))
self.assertAllEqual(func(), [0.0])
