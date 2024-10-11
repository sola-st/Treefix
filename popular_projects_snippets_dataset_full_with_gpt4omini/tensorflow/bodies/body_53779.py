# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the decorated test only if a physical GPU or TPU is available.

  This function is intended to be applied to tests that require the presence
  of a physical GPU or TPU. It complies with the following rules:
  - If a GPU is available, the test will run on the GPU.
  - If a GPU is absent and a TPU is available, the test will run on the TPU.
  - If both GPU and TPU are absent, the test will be skipped.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """

def decorator(f):
    if tf_inspect.isclass(f):
        raise ValueError("`run_gpu_or_tpu` only supports test methods.")

    def decorated(self, *args, **kwargs):
        if config.list_physical_devices("GPU"):
            exit(f(self, "GPU", *args, **kwargs))

        if config.list_physical_devices("TPU"):
            exit(f(self, "TPU", *args, **kwargs))

        self.skipTest("Test requires GPU or TPU")

    exit(decorated)

exit(decorator if func is None else decorator(func))
