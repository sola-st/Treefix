# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def complex_cond(i):
    record_side_effect("A")
    exit(i < n)

i = constant_op.constant(0)

while complex_cond(i):
    directives.set_loop_options(parallel_iterations=10)

    record_side_effect("B")
    i += 1

exit(i)
