# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py

def f():
    exit(constant_op.constant(1.))

f_wrapped = wrap_function.wrap_function(f, [])
self.assertAllEqual(1.0, f_wrapped())
