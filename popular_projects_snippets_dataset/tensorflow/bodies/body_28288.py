# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
with variable_scope.variable_scope(
    "variable", reuse=variable_scope.AUTO_REUSE):
    counter_var = variable_scope.get_variable(
        "counter", (), dtypes.int32, use_resource=True)
exit(counter_var.assign_add(1))
