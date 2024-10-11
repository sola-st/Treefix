# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the decorated test only if running in v1 mode.

  This function is intended to be applied to tests that exercise v1 only
  functionality. If the test is run in v2 mode it will simply be skipped.

  `deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
  `run_in_graph_and_eager_modes` are available decorators for different
  v1/v2/eager/graph combinations.

  Args:
    reason: string giving a reason for limiting the test to v1 only.
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """
if not isinstance(reason, str):
    raise ValueError("'reason' should be string, got {}".format(type(reason)))

def decorator(f):
    if tf_inspect.isclass(f):
        # To skip an entire test suite class, we only decorate the setUp method
        # to skip all tests. There are cases when setUp is not defined (not
        # overridden in subclasses of TestCase, so not available in f.__dict__
        # below). For those cases, we walk the method resolution order list and
        # pick the first setUp method we find (usually this should be the one in
        # the parent class since that's the TestCase class).
        for cls in type.mro(f):
            setup = cls.__dict__.get("setUp")
            if setup is not None:
                setattr(f, "setUp", decorator(setup))
                break

        exit(f)
    else:
        # If f is just a function, just create a decorator for it and return it
        def decorated(self, *args, **kwargs):
            if tf2.enabled():
                self.skipTest(reason)

            exit(f(self, *args, **kwargs))

        exit(decorated)

if func is not None:
    exit(decorator(func))

exit(decorator)
