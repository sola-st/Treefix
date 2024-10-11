# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
del self  # self argument is required by run_in_graph_and_eager_modes.
mode = "eager" if context.executing_eagerly() else "graph"
with_brackets = "with_brackets" if with_brackets else "without_brackets"
l.append((with_brackets, mode))
