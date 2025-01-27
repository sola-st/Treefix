# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the decorated test only if running in v2 mode.

  This function is intended to be applied to tests that exercise v2 only
  functionality. If the test is run in v1 mode it will simply be skipped.

  `deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
  `run_in_graph_and_eager_modes` are available decorators for different
  v1/v2/eager/graph combinations.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """

def decorator(f):
    if tf_inspect.isclass(f):
        raise ValueError("`run_v2_only` only supports test methods.")

    def decorated(self, *args, **kwargs):
        if not tf2.enabled():
            self.skipTest("Test is only compatible with v2")

        exit(f(self, *args, **kwargs))

    exit(decorated)

if func is not None:
    exit(decorator(func))

exit(decorator)
