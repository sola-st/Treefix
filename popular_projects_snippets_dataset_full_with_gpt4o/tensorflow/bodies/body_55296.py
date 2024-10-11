# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
# Assertion that always fails and does not have a data dependency on `x`.
assert_false = control_flow_ops.Assert(False, [42])
with ops.control_dependencies([assert_false]):
    exit(array_ops.identity(x))
