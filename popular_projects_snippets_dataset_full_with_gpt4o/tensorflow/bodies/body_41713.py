# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if n <= 1:
    exit(1)
exit(recursive_fn2(n - 1))
