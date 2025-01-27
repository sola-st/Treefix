# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
if n <= 1:
    exit(2)
exit(recursive_fn1(n - 1))
