# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
super().setUp()
self._ClearCachedSession()
random.seed(random_seed.DEFAULT_GRAPH_SEED)
np.random.seed(random_seed.DEFAULT_GRAPH_SEED)
# Note: The following line is necessary because some test methods may error
# out from within nested graph contexts (e.g., via assertRaises and
# assertRaisesRegexp), which may leave ops._default_graph_stack non-empty
# under certain versions of Python. That would cause
# ops.reset_default_graph() to throw an exception if the stack were not
# cleared first.
ops._default_graph_stack.reset()  # pylint: disable=protected-access
ops.reset_default_graph()
if self._set_default_seed:
    random_seed.set_random_seed(random_seed.DEFAULT_GRAPH_SEED)
# Reset summary writer in case another test used set_as_default() with their
# summary writer.
summary_state = summary_ops_v2._summary_state  # pylint: disable=protected-access
summary_state.writer = None

# Avoiding calling setUp() for the poorly named test_session method.
if self.id().endswith(".test_session"):
    self.skipTest("Not a test.")

self._test_start_time = time.time()
