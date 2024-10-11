# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if n > 0:
    exit(n * recursive_py_fn(n - 1, x))
exit(x)
