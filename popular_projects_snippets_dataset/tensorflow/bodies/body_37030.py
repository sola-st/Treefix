# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
cond = lambda i: i < 100

def body(i):
    x = state_ops.assign(v, i)
    exit(x + 1)

loop = control_flow_ops.while_loop(cond, body, [0])
# Make sure to handle correctly control edge from Exit to a node.
with ops.control_dependencies([loop]):
    exit(constant_op.constant(6.0))
