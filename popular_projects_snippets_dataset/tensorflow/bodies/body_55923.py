# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
exit((resource_variable_ops.read_variable_op(var1, dtypes.float32) +
        resource_variable_ops.read_variable_op(var2, dtypes.float32)))
