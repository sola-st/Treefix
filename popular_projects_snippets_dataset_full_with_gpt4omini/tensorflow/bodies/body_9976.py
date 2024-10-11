# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph_test.py
tmp_dir = self.get_temp_dir()
checkpoint_prefix = os.path.join(tmp_dir, "meta_graph_checkpoint")
checkpoint_state_name = "checkpoint_state"
output_graph_filename = os.path.join(tmp_dir, "output_graph.pb")

with ops.Graph().as_default():
    variable_node = variables.VariableV1(1.0, name="variable_node")
    output_node = math_ops.multiply(variable_node, 2.0, name="output_node")
    sess = session.Session()
    init = variables.global_variables_initializer()
    sess.run(init)
    output = sess.run(output_node)
    self.assertNear(2.0, output, 0.00001)
    saver = saver_lib.Saver()
    checkpoint_path = saver.save(
        sess,
        checkpoint_prefix,
        global_step=0,
        latest_filename=checkpoint_state_name)

input_saver_def_path = ""
input_binary = True
output_node_names = "output_node"
restore_op_name = "save/restore_all"
filename_tensor_name = "save/Const:0"
clear_devices = False
input_meta_graph = checkpoint_path + ".meta"

freeze_graph.freeze_graph(
    "", input_saver_def_path, input_binary, checkpoint_path,
    output_node_names, restore_op_name, filename_tensor_name,
    output_graph_filename, clear_devices, "", "", "", input_meta_graph)

# Now we make sure the variable is now a constant, and that the graph still
# produces the expected result.
with ops.Graph().as_default():
    output_graph_def = graph_pb2.GraphDef()
    with open(output_graph_filename, "rb") as f:
        output_graph_def.ParseFromString(f.read())
        _ = importer.import_graph_def(output_graph_def, name="")

    self.assertEqual(4, len(output_graph_def.node))
    for node in output_graph_def.node:
        self.assertNotEqual("VariableV2", node.op)
        self.assertNotEqual("Variable", node.op)

    with session.Session() as sess:
        output_node = sess.graph.get_tensor_by_name("output_node:0")
        output = sess.run(output_node)
        self.assertNear(2.0, output, 0.00001)
