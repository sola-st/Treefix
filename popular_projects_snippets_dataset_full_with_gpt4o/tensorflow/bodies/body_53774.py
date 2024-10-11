# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if not is_gpu_available(cuda_only=True):
    self.skipTest("Test requires CUDA GPU")

exit(f(self, *args, **kwargs))
