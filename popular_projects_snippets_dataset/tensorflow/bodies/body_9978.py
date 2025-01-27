# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph_test.py
"""Ensures partitioned variables fail cleanly with freeze graph."""
checkpoint_prefix = os.path.join(self.get_temp_dir(), "saved_checkpoint")
checkpoint_state_name = "checkpoint_state"
input_graph_name = "input_graph.pb"
output_graph_name = "output_graph.pb"

# Create a graph with partition variables. When weights are partitioned into
# a single partition, the weights variable is followed by a identity ->
# identity (an additional identity node).
partitioner = partitioned_variables.fixed_size_partitioner(1)
with ops.Graph().as_default():
    with variable_scope.variable_scope("part", partitioner=partitioner):
        batch_size, height, width, depth = 5, 128, 128, 3
        input1 = array_ops.zeros(
            (batch_size, height, width, depth), name="input1")
        input2 = array_ops.zeros(
            (batch_size, height, width, depth), name="input2")

        num_nodes = depth
        filter1 = variable_scope.get_variable("filter", [num_nodes, num_nodes])
        filter2 = array_ops.reshape(filter1, [1, 1, num_nodes, num_nodes])
        conv = nn.conv2d(
            input=input1, filter=filter2, strides=[1, 1, 1, 1], padding="SAME")
        node = math_ops.add(conv, input2, name="test/add")
        node = nn.relu6(node, name="test/relu6")

    # Save graph and checkpoints.
    sess = session.Session()
    sess.run(variables.global_variables_initializer())

    saver = saver_lib.Saver()
    checkpoint_path = saver.save(
        sess,
        checkpoint_prefix,
        global_step=0,
        latest_filename=checkpoint_state_name)
    graph_io.write_graph(sess.graph, self.get_temp_dir(), input_graph_name)

    # Ensure this graph has partition variables.
    self.assertTrue([
        tensor.name.split(":")[0]
        for op in sess.graph.get_operations()
        for tensor in op.values()
        if re.search(r"/part_\d+/", tensor.name)
    ])

# Test freezing graph doesn't make it crash.
output_node_names = "save/restore_all"
output_graph_path = os.path.join(self.get_temp_dir(), output_graph_name)

with self.assertRaises(ValueError):
    freeze_graph.freeze_graph_with_def_protos(
        input_graph_def=sess.graph_def,
        input_saver_def=None,
        input_checkpoint=checkpoint_path,
        output_node_names=output_node_names,
        restore_op_name="save/restore_all",  # default value
        filename_tensor_name="save/Const:0",  # default value
        output_graph=output_graph_path,
        clear_devices=False,
        initializer_nodes="")
