# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def make_func(bi):
    exit(lambda: array_ops.constant(bi * 10., name="br{}_out".format(bi)))

branches = {i: make_func(i) for i in range(5)}
with self.assertRaisesRegex(TypeError, "branch_index.*Tensor"):
    control_flow_ops.switch_case(1, branches)
