# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("export_graph_def")
saver1_ckpt = os.path.join(test_dir, "saver1.ckpt")
saver2_ckpt = os.path.join(test_dir, "saver2.ckpt")
graph = ops_lib.Graph()
with graph.as_default():
    with ops_lib.name_scope("hidden1"):
        variable1 = variables.VariableV1([1.0], name="variable1")
        saver1 = saver_module.Saver(var_list=[variable1])
        graph.add_to_collection(ops_lib.GraphKeys.SAVERS, saver1)

    with ops_lib.name_scope("hidden2"):
        variable2 = variables.VariableV1([2.0], name="variable2")
    saver2 = saver_module.Saver(var_list=[variable2], name="hidden2/")
    graph.add_to_collection(ops_lib.GraphKeys.SAVERS, saver2)

    with self.session(graph=graph) as sess:
        self.evaluate(variables.global_variables_initializer())
        saver1.save(sess, saver1_ckpt, write_state=False)
        saver2.save(sess, saver2_ckpt, write_state=False)

graph1 = ops_lib.Graph()
with graph1.as_default():
    var_dict1 = meta_graph.copy_scoped_meta_graph(
        from_scope="hidden1",
        to_scope="new_hidden1",
        from_graph=graph,
        to_graph=graph1)
    self.assertEqual(1, len(var_dict1))

    saver_list1 = graph1.get_collection(ops_lib.GraphKeys.SAVERS)
    self.assertEqual(1, len(saver_list1))

    with self.session(graph=graph1) as sess:
        saver_list1[0].restore(sess, saver1_ckpt)
        self.assertEqual(1.0, self.evaluate(var_dict1["variable1:0"]))

graph2 = ops_lib.Graph()
with graph2.as_default():
    var_dict2 = meta_graph.copy_scoped_meta_graph(
        from_scope="hidden2",
        to_scope="new_hidden2",
        from_graph=graph,
        to_graph=graph2)
    self.assertEqual(1, len(var_dict2))

    saver_list2 = graph2.get_collection(ops_lib.GraphKeys.SAVERS)
    self.assertEqual(1, len(saver_list2))

    with self.session(graph=graph2) as sess:
        saver_list2[0].restore(sess, saver2_ckpt)
        self.assertEqual(2.0, self.evaluate(var_dict2["variable2:0"]))
