# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.graph_mode():
    ops.reset_default_graph()
    # This doesn't push anything onto the graph stack, but it does
    # set the stack's global graph.
    global_graph = ops.get_default_graph()
    fn_graph = ops.Graph()

    # pylint: disable=protected-access
    fn_graph._building_function = True
    self.assertLen(ops._default_graph_stack.stack, 0)
    with fn_graph.as_default():
        self.assertLen(ops._default_graph_stack.stack, 1)
        with ops.init_scope():
            self.assertGreater(len(ops._default_graph_stack.stack), 1)
            dummy = constant_op.constant(1.0)
        self.assertLen(ops._default_graph_stack.stack, 1)
    # Note that the global graph is _not_ on the graph stack.
    self.assertLen(ops._default_graph_stack.stack, 0)
    # Ensure that `dummy` was added to the global graph.
    self.assertEqual(global_graph, dummy.graph)
    # pylint: enable=protected-access
