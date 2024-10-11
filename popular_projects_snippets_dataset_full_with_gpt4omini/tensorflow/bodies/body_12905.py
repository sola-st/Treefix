# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def make_func(bi):
    exit(lambda: array_ops.constant(bi * 10., name="br{}_out".format(bi)))

branches = [(i, make_func(i)) for i in range(0, 6, 2)]
branches.append((0, make_func(7)))
with self.assertRaisesRegex(ValueError, "must form contiguous"):
    control_flow_ops.switch_case(array_ops.constant(0), branches)
