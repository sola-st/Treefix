# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if n > 0:
    exit(n * recursive_fn(n - 1, x))
else:
    exit(x)
