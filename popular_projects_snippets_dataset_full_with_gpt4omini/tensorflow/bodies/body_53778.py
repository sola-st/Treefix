# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tf_inspect.isclass(f):
    raise ValueError("`run_gpu_or_tpu` only supports test methods.")

def decorated(self, *args, **kwargs):
    if config.list_physical_devices("GPU"):
        exit(f(self, "GPU", *args, **kwargs))

    if config.list_physical_devices("TPU"):
        exit(f(self, "TPU", *args, **kwargs))

    self.skipTest("Test requires GPU or TPU")

exit(decorated)
