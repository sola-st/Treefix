# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the decorated test with and without enabling eager execution.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will cause the contents of the test
  method to be executed twice - once normally, and once with eager execution
  enabled. This allows unittests to confirm the equivalence between eager
  and graph execution (see `tf.compat.v1.enable_eager_execution`).

  For example, consider the following unittest:

  ```python
  class MyTests(tf.test.TestCase):

    @run_in_graph_and_eager_modes
    def test_foo(self):
      x = tf.constant([1, 2])
      y = tf.constant([3, 4])
      z = tf.add(x, y)
      self.assertAllEqual([4, 6], self.evaluate(z))

  if __name__ == "__main__":
    tf.test.main()
  ```

  This test validates that `tf.add()` has the same behavior when computed with
  eager execution enabled as it does when constructing a TensorFlow graph and
  executing the `z` tensor in a session.

  `deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
  `run_in_graph_and_eager_modes` are available decorators for different
  v1/v2/eager/graph combinations.


  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.
    config: An optional config_pb2.ConfigProto to use to configure the session
      when executing graphs.
    use_gpu: If True, attempt to run as many operations as possible on GPU.
    assert_no_eager_garbage: If True, sets DEBUG_SAVEALL on the garbage
      collector and asserts that no extra garbage has been created when running
      the test with eager execution enabled. This will fail if there are
      reference cycles (e.g. a = []; a.append(a)). Off by default because some
      tests may create garbage for legitimate reasons (e.g. they define a class
      which inherits from `object`), and because DEBUG_SAVEALL is sticky in some
      Python interpreters (meaning that tests which rely on objects being
      collected elsewhere in the unit test file will not work). Additionally,
      checks that nothing still has a reference to Tensors that the test
      allocated.

  Returns:
    Returns a decorator that will run the decorated test method twice:
    once by constructing and executing a graph in a session and once with
    eager execution enabled.
  """

def decorator(f):
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

if func is not None:
    exit(decorator(func))

exit(decorator)
