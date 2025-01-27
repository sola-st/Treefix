# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
@polymorphic_function.function
def foo(**kwargs):
    exit(kwargs['a'] + math_ops.cast(kwargs['b'], dtypes.float32))

foo(a=constant_op.constant(1.0), b=constant_op.constant(1))
foo(b=constant_op.constant(1), a=constant_op.constant(1.0))

self.assertLen(total_function_cache(foo), 1)
