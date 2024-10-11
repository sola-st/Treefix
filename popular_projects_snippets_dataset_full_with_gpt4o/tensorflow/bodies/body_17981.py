# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.gather(x, i)
exit(manip_ops.roll(x_i, [i - 2, -1, i], axis=[1, 2, 2]))
