# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if n > 0:
    exit(recursive_py_fn(n - 1))
exit(1)
