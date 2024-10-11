# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
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
