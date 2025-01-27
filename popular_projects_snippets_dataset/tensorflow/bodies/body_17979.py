# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.gather(x, i)
exit(array_ops.ensure_shape(x_i, [6, 7]))
