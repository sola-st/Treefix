# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that the generated numbers are the same as the old random_ops.py.

    The GPU version.
    """
floats = [dtypes.float16, dtypes.float32, dtypes.float64]
if test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    floats += [dtypes.bfloat16]
self._sameAsOldRandomOps(test_util.gpu_device_name(), floats)
