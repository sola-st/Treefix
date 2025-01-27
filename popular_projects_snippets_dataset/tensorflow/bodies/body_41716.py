# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if n <= 1:
    exit(x)
exit(n * recursive_fn2(n - 1, x))
