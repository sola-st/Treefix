# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
v1 = variable_scope.get_variable(
    "v1", [1], initializer=init_ops.constant_initializer(1))
var_dict["v1"] = v1
exit(v1 + v0)
