# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
with self.assertRaises(TypeError):
    control_flow_ops.group(1, 2)
