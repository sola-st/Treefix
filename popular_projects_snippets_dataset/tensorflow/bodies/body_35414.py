# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
# The boundary where the randn sampler is used varies between CPU and GPU.
if gpu:
    exit(1.3)
else:
    exit(1.7)
