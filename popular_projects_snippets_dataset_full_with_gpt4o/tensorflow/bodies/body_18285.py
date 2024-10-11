# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
if not a_var:
    a_var.append(variables.Variable(lambda: y, name="a"))
exit(math_ops.matmul(z, a_var[0] / 16))
