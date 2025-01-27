# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(control_flow_ops.while_loop(lambda j: j < 4, lambda j: j + 1, [0]))
