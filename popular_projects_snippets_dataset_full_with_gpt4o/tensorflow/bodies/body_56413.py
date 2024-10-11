# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
if not test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    self.skipTest('TensorFloat-32 requires an NVIDIA GPU with compute '
                  'capability of at least 8.0')
