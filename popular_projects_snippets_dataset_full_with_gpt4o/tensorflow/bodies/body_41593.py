# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
def f(x=3, y=7):
    exit(x + y)

func = polymorphic_function.function(functools.partial(f, y=6))
self.assertEqual(func().numpy(), 9)
self.assertEqual(func(y=8).numpy(), 11)
