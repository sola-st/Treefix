# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tf_inspect.isclass(f):
    raise ValueError("`run_gpu_only` only supports test methods.")

def decorated(self, *args, **kwargs):
    if not is_gpu_available():
        self.skipTest("Test requires GPU")

    exit(f(self, *args, **kwargs))

exit(decorated)
