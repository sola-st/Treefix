# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if n <= 1:
    exit(2 * x)
exit(n * recursive_fn1(n - 1, x))
