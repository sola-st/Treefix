# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(control_flow_ops.cond(y > split, lambda: f(x, y), lambda:
                             (x + 1., y)))
