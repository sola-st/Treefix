# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
var = variable_scope.get_variable(
    "var",
    shape=[10],
    dtype=dtypes.float32,
    initializer=init_ops.ones_initializer())
exit(inputs + var)
