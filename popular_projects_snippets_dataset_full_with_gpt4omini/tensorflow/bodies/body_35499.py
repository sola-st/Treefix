# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
float_types = [dtypes.float16, dtypes.float32, dtypes.float64]
if test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    float_types += [dtypes.bfloat16]
exit(float_types)
