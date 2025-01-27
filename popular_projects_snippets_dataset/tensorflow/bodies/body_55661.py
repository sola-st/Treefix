# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph1 = ops.Graph()
with graph1.as_default():
    a = constant_op.constant(1.0, shape=[2, 2])
    b = constant_op.constant(2.0, shape=[2, 2])
    matmul = math_ops.matmul(a, b)
    with ops.name_scope("hidden1"):
        c = nn_ops.relu(matmul)
        d = constant_op.constant(3.0, shape=[2, 2])
        matmul = math_ops.matmul(c, d)

orig_meta_graph, _ = meta_graph.export_scoped_meta_graph(
    export_scope="hidden1", graph=graph1)

graph2 = ops.Graph()
with graph2.as_default():
    with self.assertRaisesRegex(ValueError, "Graph contains unbound inputs"):
        meta_graph.import_scoped_meta_graph(
            orig_meta_graph, import_scope="new_hidden1")

    meta_graph.import_scoped_meta_graph(
        orig_meta_graph,
        import_scope="new_hidden1",
        input_map={
            "$unbound_inputs_MatMul": constant_op.constant(
                4.0, shape=[2, 2])
        })
