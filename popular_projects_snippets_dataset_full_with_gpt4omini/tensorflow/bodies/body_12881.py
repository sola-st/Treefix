# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
nbranches = 5

def make_func(bi):
    exit(lambda: array_ops.constant(bi * 10, name="br{}_out".format(bi)))

branches = [(i, make_func(i)) for i in range(nbranches)]
for bi in range(nbranches):
    branch_index = array_ops.placeholder_with_default(bi, [])
    case_out = control_flow_ops.switch_case(branch_index, branches)
    self.assertEqual(bi * 10, self.evaluate(case_out))
