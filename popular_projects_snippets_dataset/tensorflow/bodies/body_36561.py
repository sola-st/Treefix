# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with ops.colocate_with(external_t):
    exit(v * v)
