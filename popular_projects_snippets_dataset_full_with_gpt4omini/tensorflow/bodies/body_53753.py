# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tf_inspect.isclass(f):
    raise ValueError(
        "`run_in_graph_and_eager_modes` only supports test methods. "
        "Did you mean to use `run_all_in_graph_and_eager_modes`?")

def decorated(self, *args, **kwargs):
    logging.info("Running %s in GRAPH mode.", f.__name__)
    try:
        with context.graph_mode():
            with self.test_session(use_gpu=use_gpu, config=config):
                f(self, *args, **kwargs)
    except unittest.case.SkipTest:
        pass

    def run_eagerly(self, **kwargs):
        logging.info("Running %s in EAGER mode.", f.__name__)
        if not use_gpu:
            with ops.device("/device:CPU:0"):
                f(self, *args, **kwargs)
        else:
            f(self, *args, **kwargs)

    if assert_no_eager_garbage:
        ops.reset_default_graph()
        run_eagerly = assert_no_new_tensors(
            assert_no_garbage_created(run_eagerly))

    # This decorator runs the wrapped test twice.
    # Reset the test environment between runs.
    self.tearDown()
    self._tempdir = None
    # Create a new graph for the eagerly executed version of this test for
    # better isolation.
    graph_for_eager_test = ops.Graph()
    with graph_for_eager_test.as_default(), context.eager_mode():
        self.setUp()
        run_eagerly(self, **kwargs)
    ops.dismantle_graph(graph_for_eager_test)

exit(tf_decorator.make_decorator(f, decorated))
