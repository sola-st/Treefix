# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
with ops.control_dependencies(
    [control_flow_ops.Assert(math_ops.less_equal(x, 10.0), [x])]):
    exit(array_ops.identity(x))
