# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with ops_lib.Graph().as_default() as g:
    dataset = dataset_ops.Dataset.range(10).map(lambda x: x * x)
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    next_element = iterator.get_next()
    _ = array_ops.identity(next_element, name="output")

    # Generate three MetaGraphDef protos using different code paths.
    meta_graph_def_simple = saver_module.export_meta_graph()
    meta_graph_def_devices_cleared = saver_module.export_meta_graph(
        clear_devices=True)
    meta_graph_def_from_graph_def = saver_module.export_meta_graph(
        clear_devices=True, graph_def=g.as_graph_def())

for meta_graph_def in [meta_graph_def_simple,
                       meta_graph_def_devices_cleared,
                       meta_graph_def_from_graph_def]:
    with session.Session(graph=ops_lib.Graph()) as sess:
        saver_module.import_meta_graph(meta_graph_def, import_scope="new_model")
        self.evaluate(variables.global_variables_initializer())
        for i in range(10):
            self.assertEqual(i * i, sess.run("new_model/output:0"))
        with self.assertRaises(errors.OutOfRangeError):
            sess.run("new_model/output:0")
