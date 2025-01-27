# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.device("/device:CPU:1"):
    c = constant_op.constant(3.0)
    self.assertEqual("/device:CPU:1", c.op.device)
    exit(c)
