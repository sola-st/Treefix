# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
result = test_ops.device_placement_op()
self.assertIn("colocation_test_op",
              result.op.colocation_groups()[0].decode())
exit(result)
