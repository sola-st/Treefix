# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
local_op = test_ops.device_placement_op()
with ops.device("/job:localhost/CPU:0"):
    worker_op = test_ops.device_placement_op()
exit((local_op, worker_op))
