# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Save from graph mode and restore from eager mode.
graph_ckpt_prefix = os.path.join(self.get_temp_dir(), "graph_ckpt")
with context.graph_mode():
    with self.session(graph=ops_lib.Graph()) as sess:
        # Create a graph model and save the checkpoint.
        w1 = resource_variable_ops.ResourceVariable(1.0, name="w1")
        w2 = resource_variable_ops.ResourceVariable(2.0, name="w2")
        graph_saver = saver_module.Saver([w1, w2])
        self.evaluate(variables.global_variables_initializer())
        graph_saver.save(sess, graph_ckpt_prefix)

with context.eager_mode():
    ops_lib._default_graph_stack.reset()  # pylint: disable=protected-access
    ops_lib.reset_default_graph()

    w1 = resource_variable_ops.ResourceVariable(0.0, name="w1")
    w2 = resource_variable_ops.ResourceVariable(0.0, name="w2")

    graph_saver = saver_module.Saver([w1, w2])
    graph_saver.restore(None, graph_ckpt_prefix)

    self.assertAllEqual(self.evaluate(w1), 1.0)
    self.assertAllEqual(self.evaluate(w2), 2.0)

# Save from eager mode and restore from graph mode.
eager_ckpt_prefix = os.path.join(self.get_temp_dir(), "eager_ckpt")
with context.eager_mode():
    ops_lib._default_graph_stack.reset()  # pylint: disable=protected-access
    ops_lib.reset_default_graph()

    w3 = resource_variable_ops.ResourceVariable(3.0, name="w3")
    w4 = resource_variable_ops.ResourceVariable(4.0, name="w4")

    graph_saver = saver_module.Saver([w3, w4])
    graph_saver.save(None, eager_ckpt_prefix)

with context.graph_mode():
    with self.session(graph=ops_lib.Graph()) as sess:
        w3 = resource_variable_ops.ResourceVariable(0.0, name="w3")
        w4 = resource_variable_ops.ResourceVariable(0.0, name="w4")
        graph_saver = saver_module.Saver([w3, w4])
        self.evaluate(variables.global_variables_initializer())
        graph_saver.restore(sess, eager_ckpt_prefix)
        self.assertAllEqual(w3, 3.0)
        self.assertAllEqual(w4, 4.0)
