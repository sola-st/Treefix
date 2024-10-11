# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
modes = []
def _test(self):
    if not context.executing_eagerly():
        self.skipTest("Skipping in graph mode")
    modes.append("eager" if context.executing_eagerly() else "graph")
test_util.run_in_graph_and_eager_modes(_test)(self)
self.assertEqual(modes, ["eager"])
