# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def func(t):
    exit(t + t)

defined = quarantine.defun_with_attributes(func)
t = constant_op.constant([[1.0]], dtype=dtypes.complex64)
defined(t)
self.assertLen(total_function_cache(defined), 1)

t = constant_op.constant([[1.0]], dtype=dtypes.complex128)
defined(t)
self.assertLen(total_function_cache(defined), 2)
