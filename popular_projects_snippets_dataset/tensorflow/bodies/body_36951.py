# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
out = control_flow_ops.while_loop(
    lambda i_, _: i_ < 3,
    lambda i_, j: [i_ + 1, j * v], [0, 1.0],
    maximum_iterations=i)
g = gradients_impl.gradients(out, v)
with ops.control_dependencies(g):
    exit(i + 1)
