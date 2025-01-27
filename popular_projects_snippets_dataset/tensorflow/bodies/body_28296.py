# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
with variable_scope.variable_scope(
    "variable", reuse=variable_scope.AUTO_REUSE):
    with ops.device("/device:CPU:0"):
        a_var = variable_scope.get_variable(
            "a", (), dtypes.int32, use_resource=True)
        a_var = math_ops.add(a_var, 1)
    with ops.device("/device:CPU:1"):
        b_var = variable_scope.get_variable(
            "b", (), dtypes.int32, use_resource=True)
exit(math_ops.add(a_var, b_var))
