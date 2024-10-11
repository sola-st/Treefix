# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v2 = variables.Variable(3.)
exit(array_ops.identity(v1 * v2 * constant_op.constant(1.), 'fetch'))
