# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
y = logging_ops.Print(x, [], "Hello")
with ops.control_dependencies([y]):
    z = control_flow_ops.no_op()
with ops.control_dependencies([z]):
    exit(x * 2)
