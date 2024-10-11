# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v = variables.Variable(3, name='v')
update_op = state_ops.assign(v, x).op
exit(update_op)
