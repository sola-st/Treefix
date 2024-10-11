# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph_test.py
tmp_dir = self.get_temp_dir()
saved_model_dir = os.path.join(tmp_dir, "saved_model_dir")
feature_name = "feature"
self._writeDummySavedModel(saved_model_dir, feature_name, tags_list)
output_graph_filename = os.path.join(tmp_dir, "output_graph.pb")

input_saved_model_dir = saved_model_dir
output_node_names = "output_node"
input_binary = False
input_saver_def_path = False
restore_op_name = None
filename_tensor_name = None
clear_devices = False
input_meta_graph = False
checkpoint_path = None
input_graph_filename = None
saved_model_tags = tags_string

freeze_graph.freeze_graph(input_graph_filename, input_saver_def_path,
                          input_binary, checkpoint_path, output_node_names,
                          restore_op_name, filename_tensor_name,
                          output_graph_filename, clear_devices, "", "", "",
                          input_meta_graph, input_saved_model_dir,
                          saved_model_tags)

# Now we make sure the variable is now a constant, and that the graph still
# produces the expected result.
with ops.Graph().as_default():
    output_graph_def = graph_pb2.GraphDef()
    with open(output_graph_filename, "rb") as f:
        output_graph_def.ParseFromString(f.read())
        _ = importer.import_graph_def(output_graph_def, name="")

    if any(u"ParseExampleV2" in node.name for node in output_graph_def.node):
        expected_node_count = 10
    else:
        expected_node_count = 8
    self.assertEqual(expected_node_count, len(output_graph_def.node))
    for node in output_graph_def.node:
        self.assertNotEqual("VariableV2", node.op)
        self.assertNotEqual("Variable", node.op)

    feature_value = 2.0
    example = self._createTFExampleString(feature_name, feature_value)
    with session.Session() as sess:
        input_node = sess.graph.get_tensor_by_name("input_node:0")
        output_node = sess.graph.get_tensor_by_name("output_node:0")
        output = sess.run(output_node, feed_dict={input_node: [example]})
        self.assertNear(feature_value, output, 0.00001)
