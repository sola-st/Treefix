# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.device("/job:localhost"):
    exit(functional_op_to_test(_fn))
