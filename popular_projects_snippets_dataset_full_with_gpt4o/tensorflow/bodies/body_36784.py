# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
self.assertEqual("/job:localhost/device:GPU:0",
                 constant_op.constant(3.0).op.device)
exit(test_ops.device_placement_op())
