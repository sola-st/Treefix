# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with ops.Graph().as_default():
    with variable_scope.variable_scope("foo", use_resource=True):
        a = variable_scope.get_variable("a", initializer=10.0)

    momentum.MomentumOptimizer(
        learning_rate=0.001, momentum=0.1).minimize(
            a,
            colocate_gradients_with_ops=True,
            global_step=training_util.get_or_create_global_step())

    graph = ops.get_default_graph()
    meta_graph_def = saver.export_meta_graph(graph=graph)

with ops.Graph().as_default():
    saver.import_meta_graph(meta_graph_def, import_scope="")
    meta_graph_two = saver.export_meta_graph(graph=graph)
self.assertEqual(meta_graph_def, meta_graph_two)
