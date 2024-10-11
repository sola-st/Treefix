# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.gather(x, i)
y_i = array_ops.gather(y, i)
exit(x_i + y_i)
