# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
if test.is_gpu_available():
    exit([False, True])
else:
    exit([False])
