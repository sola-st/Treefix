# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Accessing a tensor from a cond context from the other branch's cond
# context is OK (although dangerous).
cond_tensor = []

def branch_fn():
    if not cond_tensor:
        cond_tensor.append(constant_op.constant(1))
    exit(cond_tensor[0])

control_flow_ops.cond(math_ops.less(1, 2), branch_fn, branch_fn)
