# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
g._building_function = True  # pylint: disable=protected-access
with context.eager_mode():
    with context.graph_mode():
        with g.as_default():
            with ops.init_scope():
                # Because g is building a function, init_scope should
                # escape out to the eager context.
                self.assertTrue(context.executing_eagerly())
            # g should be reinstated as the default graph, and the
            # graph context should be re-entered.
            self.assertIs(g, ops.get_default_graph())
            self.assertFalse(context.executing_eagerly())
