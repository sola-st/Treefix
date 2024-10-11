# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    g = ops.Graph()
    with g.as_default():
        with ops.init_scope():
            self.assertFalse(context.executing_eagerly())
            self.assertEqual(g, ops.get_default_graph())
