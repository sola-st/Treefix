# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if not is_gpu_available():
    self.skipTest("Test requires GPU")

exit(f(self, *args, **kwargs))
