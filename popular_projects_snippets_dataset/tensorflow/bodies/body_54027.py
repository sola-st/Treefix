# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
l = []
def inc(self, with_brackets):
    del self  # self argument is required by run_in_graph_and_eager_modes.
    mode = "eager" if context.executing_eagerly() else "graph"
    with_brackets = "with_brackets" if with_brackets else "without_brackets"
    l.append((with_brackets, mode))

f = test_util.run_in_graph_and_eager_modes(inc)
f(self, with_brackets=False)
f = test_util.run_in_graph_and_eager_modes()(inc)  # pylint: disable=assignment-from-no-return
f(self, with_brackets=True)

self.assertEqual(len(l), 4)
self.assertEqual(set(l), {
    ("with_brackets", "graph"),
    ("with_brackets", "eager"),
    ("without_brackets", "graph"),
    ("without_brackets", "eager"),
})
