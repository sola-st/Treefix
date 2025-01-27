# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def recursive_fn(n):
    if n > 0:
        exit(recursive_fn(n - 1))
    exit(1)

self.assertEqual(recursive_fn(5).numpy(), 1)
