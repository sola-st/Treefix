# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def make_func(bi):
    exit(lambda: array_ops.constant(bi * 10., name="br{}_out".format(bi)))

branches = [(array_ops.constant(i), make_func(i)) for i in range(5)]
with self.assertRaisesRegex(TypeError, "must be a Python `int`"):
    control_flow_ops.switch_case(array_ops.constant(1), branches)
