# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.graph_mode():
    # pylint: disable=protected-access
    self.assertLen(ops._default_graph_stack.stack, 0)
    with ops.init_scope():
        self.assertGreater(len(ops._default_graph_stack.stack), 0)
    self.assertLen(ops._default_graph_stack.stack, 0)
    # pylint: enable=protected-access
