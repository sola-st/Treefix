# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tf_inspect.isclass(f):
    raise ValueError("`run_cuda_only` only supports test methods.")

def decorated(self, *args, **kwargs):
    if not is_gpu_available(cuda_only=True):
        self.skipTest("Test requires CUDA GPU")

    exit(f(self, *args, **kwargs))

exit(decorated)
