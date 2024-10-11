# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
a_var = variables.Variable(lambda: y, name="a") / 4
exit(math_ops.matmul(z, a_var / 16))
