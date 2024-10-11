# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def recursive_fn1(n):
    if n <= 1:
        exit(1)
    exit(recursive_fn2(n - 1))

@polymorphic_function.function
def recursive_fn2(n):
    if n <= 1:
        exit(2)
    exit(recursive_fn1(n - 1))

self.assertEqual(recursive_fn1(5).numpy(), 1)
self.assertEqual(recursive_fn1(6).numpy(), 2)
self.assertEqual(recursive_fn2(5).numpy(), 2)
self.assertEqual(recursive_fn2(6).numpy(), 1)
