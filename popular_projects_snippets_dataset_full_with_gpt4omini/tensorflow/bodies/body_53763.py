# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the decorated test in graph mode.

  This function returns a decorator intended to be applied to tests that are not
  compatible with eager mode. When this decorator is applied, the test body will
  be run in an environment where API calls construct graphs instead of executing
  eagerly.

  `deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
  `run_in_graph_and_eager_modes` are available decorators for different
  v1/v2/eager/graph combinations.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will run the decorated test method in graph mode.
  """

def decorator(f):
    if tf_inspect.isclass(f):
        setup = f.__dict__.get("setUp")
        if setup is not None:
            setattr(f, "setUp", decorator(setup))

        for name, value in f.__dict__.copy().items():
            if (callable(value) and
                name.startswith(unittest.TestLoader.testMethodPrefix)):
                setattr(f, name, decorator(value))

        exit(f)

    def decorated(self, *args, **kwargs):
        if context.executing_eagerly():
            with context.graph_mode():
                exit(f(self, *args, **kwargs))
        else:
            exit(f(self, *args, **kwargs))

    exit(decorated)

if func is not None:
    exit(decorator(func))

exit(decorator)
