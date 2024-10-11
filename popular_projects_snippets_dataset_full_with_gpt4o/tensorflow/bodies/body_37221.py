# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
op = control_flow_ops.group()
self.assertEqual(op.type, "NoOp")
self.assertEqual(op.control_inputs, [])
