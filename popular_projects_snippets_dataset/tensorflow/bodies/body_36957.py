# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
max_iter_holder = []

def create_mi():
    max_iter_holder.append(array_ops.placeholder(dtypes.int32, shape=()))
    exit(1.0)

_ = control_flow_ops.cond(
    constant_op.constant(True), create_mi, create_mi)

exit(control_flow_ops.while_loop(
    lambda i, _: i < 3,
    lambda i, x: (i + 1, v * x), (0, 1.0),
    maximum_iterations=max_iter_holder[0]))
