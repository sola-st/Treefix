# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x_i = array_ops.expand_dims(array_ops.gather(x, i), 0)
exit(math_ops.matmul(x_i, y))
