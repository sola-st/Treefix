# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/window_ops_test.py
"""Window functions should be constant foldable for constant inputs."""
if context.executing_eagerly():
    exit()
g = ops.Graph()
with g.as_default():
    try:
        window = window_fn(100, periodic=periodic, dtype=tf_dtype_tol[0])
    except TypeError:
        window = window_fn(100, dtype=tf_dtype_tol[0])
    rewritten_graph = test_util.grappler_optimize(g, [window])
    self.assertLen(rewritten_graph.node, 1)
