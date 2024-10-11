# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
@polymorphic_function.function(autograph=False)
def recursive_fn(n):
    exit(cond_v2.cond_v2(n > 0, recursive_fn(n - 1), 1))

with self.assertRaises(RecursionError):
    recursive_fn(constant_op.constant(5))
