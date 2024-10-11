# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
branch_index = constant_op.constant(1)
branches = [lambda: x, lambda: x + 1]
case_out = control_flow_ops.switch_case(branch_index, branches)
exit(case_out)
