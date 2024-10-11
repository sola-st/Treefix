# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with ops.device("cpu:0"):
    next_i, branch_out = control_flow_ops.switch_case(i, make_branches(i))
exit((next_i, result + branch_out))
