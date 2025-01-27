# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
cpu_zero_op = test_ops.device_placement_op()
self.assertEqual("/job:localhost/device:CPU:0", cpu_zero_op.device)
with ops.device("CPU:1"):
    cpu_one_op = test_ops.device_placement_op()
    self.assertEqual("/job:localhost/device:CPU:1", cpu_one_op.device)
exit((cpu_zero_op, cpu_one_op))
