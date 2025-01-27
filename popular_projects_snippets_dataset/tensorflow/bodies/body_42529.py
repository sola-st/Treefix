# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v3 = variables.Variable(4.)
v3_holder.append(v3)
ops.add_to_collection(ops.GraphKeys.LOSSES, v3 * constant_op.constant(3.))
exit(array_ops.identity(v1 * v3 * constant_op.constant(1.), 'fetch'))
