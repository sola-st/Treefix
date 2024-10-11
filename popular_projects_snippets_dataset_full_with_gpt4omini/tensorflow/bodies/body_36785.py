# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.device("/job:localhost/device:GPU:0"):
    exit(cond_v2.cond_v2(constant_op.constant(True), fn2, fn2))
