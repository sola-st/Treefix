# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph = ops.Graph()
# Create all the missing inputs.
with graph.as_default():
    new_image = constant_op.constant(
        1.2, dtypes.float32, shape=[100, 28], name="images")

with self.assertRaisesRegex(ValueError, "Graph contains unbound inputs"):
    meta_graph.import_scoped_meta_graph(
        os.path.join(test_dir, exported_filenames[0]),
        graph=graph,
        import_scope="new_hidden1")

with self.assertRaisesRegex(ValueError, "Graph contains unbound inputs"):
    meta_graph.import_scoped_meta_graph(
        os.path.join(test_dir, exported_filenames[0]),
        graph=graph,
        input_map={"image:0": new_image},
        import_scope="new_hidden1")

# Verifies we can import the original "hidden1" into "new_hidden1".
var_list = meta_graph.import_scoped_meta_graph(
    os.path.join(test_dir, exported_filenames[0]),
    graph=graph,
    input_map={"$unbound_inputs_images": new_image},
    import_scope="new_hidden1")

self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))
new_var_names = [v.name for _, v in var_list.items()]
self.assertEqual(["new_hidden1/biases:0", "new_hidden1/weights:0"],
                 sorted(new_var_names))

# Verifies we can import the original "hidden2" into "new_hidden2".
hidden1 = array_ops.identity(
    graph.as_graph_element("new_hidden1/Relu:0"), name="hidden1/Relu")
var_list = meta_graph.import_scoped_meta_graph(
    os.path.join(test_dir, exported_filenames[1]),
    graph=graph,
    input_map={"$unbound_inputs_hidden1/Relu": hidden1},
    import_scope="new_hidden2",
    unbound_inputs_col_name=None)

self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))
new_var_names = [v.name for _, v in var_list.items()]
self.assertEqual(["new_hidden2/biases:0", "new_hidden2/weights:0"],
                 sorted(new_var_names))

# Verifies we can import the original "softmax_linear" into
# "new_softmax_linear".
hidden2 = array_ops.identity(
    graph.as_graph_element("new_hidden2/Relu:0"), name="hidden2/Relu")
var_list = meta_graph.import_scoped_meta_graph(
    os.path.join(test_dir, exported_filenames[2]),
    graph=graph,
    input_map={"$unbound_inputs_hidden2/Relu": hidden2},
    import_scope="new_softmax_linear",
    unbound_inputs_col_name=None)
self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))
new_var_names = [v.name for _, v in var_list.items()]
self.assertEqual(
    ["new_softmax_linear/biases:0", "new_softmax_linear/weights:0"],
    sorted(new_var_names))

# Exports the scoped meta graphs again.
new_meta_graph1, var_list = meta_graph.export_scoped_meta_graph(
    graph=graph, export_scope="new_hidden1")
self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))

new_meta_graph2, var_list = meta_graph.export_scoped_meta_graph(
    graph=graph, export_scope="new_hidden2", unbound_inputs_col_name=None)
self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))

new_meta_graph3, var_list = meta_graph.export_scoped_meta_graph(
    graph=graph,
    export_scope="new_softmax_linear",
    unbound_inputs_col_name=None)
self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))

exit([new_meta_graph1, new_meta_graph2, new_meta_graph3])
