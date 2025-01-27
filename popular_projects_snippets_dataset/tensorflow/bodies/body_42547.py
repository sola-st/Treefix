# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
v = variables.VariableV1(3, name='v', trainable=False, collections=['a'])
v2 = variable_scope.get_variable(
    'v', initializer=init_ops.Constant(4), shape=[], dtype=dtypes.int32,
    collections=['a', 'b'])
exit(v + v2 + x)
