# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
v2 = variable_scope.get_variable(
    "v2", [1], initializer=init_ops.constant_initializer(2))
var_dict["v2"] = v2
exit(v2 + v0)
