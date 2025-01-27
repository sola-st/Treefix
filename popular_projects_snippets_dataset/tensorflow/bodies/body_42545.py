# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v = variables.Variable(3, name='v')
v2 = variable_scope.get_variable(
    'v', initializer=init_ops.Constant(4), shape=[], dtype=dtypes.int32)
exit(v + v2 + x)
