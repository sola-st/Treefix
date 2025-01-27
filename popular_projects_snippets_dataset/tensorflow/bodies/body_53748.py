# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Run a test case in v1 graph mode and inside tf.function in eager mode.

  WARNING: This decorator can only be used in test cases that statically checks
  generated graph. Attempting to evaluate graph or function results via.
  session.run() or self.evaluate() will fail.

  WARNING: This decorator can only be used for test cases that inherit from
  absl.testing.parameterized.TestCase.

  Args:
    func: Test case function to be decorated.

  Returns:
    Decorated test case function.
  """

def decorator(f):
    if tf_inspect.isclass(f):
        raise ValueError(
            "`run_in_graph_mode_and_function` only supports test methods.")

    @parameterized.named_parameters(("_v1_graph", "v1_graph"),
                                    ("_function", "function"))
    @functools.wraps(f)
    def decorated(self, run_mode, *args, **kwargs):
        if run_mode == "v1_graph":
            with ops.Graph().as_default():
                f(self, *args, **kwargs)
        elif run_mode == "function":

            @def_function.function
            def function_in_eager():
                f(self, *args, **kwargs)

            # Create a new graph for the eagerly executed version of this test for
            # better isolation.
            graph_for_eager_test = ops.Graph()
            with graph_for_eager_test.as_default(), context.eager_mode():
                function_in_eager()
            ops.dismantle_graph(graph_for_eager_test)
        else:
            raise ValueError("Unknown run mode %s" % run_mode)

    exit(decorated)

if func is not None:
    exit(decorator(func))

exit(decorator)
