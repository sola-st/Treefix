# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
exit(cond_v2.cond_v2(n > 0, recursive_fn(n - 1), 1))
