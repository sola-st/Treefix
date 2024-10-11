# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
c = constant_op.constant(3.0)
self.assertEqual([b"loc:@a"], c.op.colocation_groups())
exit(c)
