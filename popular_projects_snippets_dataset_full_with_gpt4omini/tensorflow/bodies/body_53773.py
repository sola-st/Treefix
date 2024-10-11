# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the decorated test only if a GPU is available.

  This function is intended to be applied to tests that require the presence
  of a GPU. If a GPU is absent, it will simply be skipped.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """

def decorator(f):
    if tf_inspect.isclass(f):
        raise ValueError("`run_gpu_only` only supports test methods.")

    def decorated(self, *args, **kwargs):
        if not is_gpu_available():
            self.skipTest("Test requires GPU")

        exit(f(self, *args, **kwargs))

    exit(decorated)

if func is not None:
    exit(decorator(func))

exit(decorator)
