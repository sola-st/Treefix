# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

a = 0
b = 1

i = constant_op.constant(0)
while i < n:
    directives.set_loop_options(parallel_iterations=10)
    i += 1
    a += 2
    b *= 3

exit((i, a, b))
