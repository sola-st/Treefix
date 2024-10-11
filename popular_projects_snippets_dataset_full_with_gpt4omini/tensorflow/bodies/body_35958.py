# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
v = variable_scope.get_variable("v", shape=[3, 4], dtype=dtypes.float32)
# Ensure it is possible to do get_variable with a _ref dtype passed in.
_ = variable_scope.get_variable("w", shape=[5, 6], dtype=v.dtype)
