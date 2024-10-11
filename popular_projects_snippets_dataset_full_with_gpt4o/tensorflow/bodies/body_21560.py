# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Save a simple graph that contains no variables into a checkpoint.
test_dir = self._get_test_dir("no_vars_graph")
filename = os.path.join(test_dir, "ckpt")
graph_1 = ops_lib.Graph()
with session.Session(graph=graph_1) as sess:
    constant_op.constant([1, 2, 3], name="x")
    constant_op.constant([1, 2, 3], name="y")
    saver = saver_module.Saver(allow_empty=True)
    saver.save(sess, filename)

# Create a fresh graph.
graph_2 = ops_lib.Graph()
with session.Session(graph=graph_2) as sess:
    # Restore the above checkpoint under scope "subgraph_1".
    new_saver_1 = saver_module.import_meta_graph(
        filename + ".meta", graph=graph_2, import_scope="subgraph_1")
    # There are no variables to restore, so import_meta_graph should not
    # return a Saver.
    self.assertIsNone(new_saver_1)

    # Create a variable in graph_2 under scope "my_scope".
    variables.VariableV1(array_ops.zeros([10]), name="my_scope/my_var")
    self.evaluate(variables.global_variables_initializer())
    # Restore the checkpoint into a different scope "subgraph_2".
    new_saver_2 = saver_module.import_meta_graph(
        filename + ".meta", graph=graph_2, import_scope="subgraph_2")
    # Because the variable does not live in scope "subgraph_2",
    # import_meta_graph should not attempt to restore the variable. So,
    # import_meta_graph still won't return a Saver instance.
    self.assertIsNone(new_saver_2)

    # However, if we restore the checkpoint under scope "my_scope",
    # import_meta_graph will detect the variable and return a Saver for
    # restoring it. This should happen even when the variable does not
    # originate from graph_1.
    new_saver_3 = saver_module.import_meta_graph(
        filename + ".meta", graph=graph_2, import_scope="my_scope")
    self.assertIsInstance(new_saver_3, saver_module.Saver)
