# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
with variable_scope.variable_scope(
    'reuse', reuse=variable_scope.AUTO_REUSE):
    v = variable_scope.get_variable(
        'v', initializer=init_ops.Constant(4), shape=[], dtype=dtypes.int32)
exit(v - x)
