# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph = ops.Graph()
with graph.as_default():
    # Creates an inference graph.
    # Hidden 1
    colocate_constraint = constant_op.constant(1.2, name="constraint")
    images = constant_op.constant(
        1.2, dtypes.float32, shape=[100, 28], name="images")
    with ops.name_scope("hidden1"):
        with graph.colocate_with(colocate_constraint.op):
            weights1 = variables.Variable(
                random_ops.truncated_normal(
                    [28, 128], stddev=1.0 / math.sqrt(float(28))),
                name="weights")
        # The use of control_flow_ops.cond here is purely for adding test
        # coverage the save and restore of control flow context (which doesn't
        # make any sense here from a machine learning perspective).  The typical
        # biases is a simple Variable without the conditions.
        biases1 = variables.Variable(
            control_flow_ops.cond(
                math_ops.less(random.random(), 0.5),
                lambda: array_ops.ones([128]), lambda: array_ops.zeros([128])),
            name="biases")
        hidden1 = nn_ops.relu(math_ops.matmul(images, weights1) + biases1)

    # Hidden 2
    with ops.name_scope("hidden2"):
        weights2 = variables.Variable(
            random_ops.truncated_normal(
                [128, 32], stddev=1.0 / math.sqrt(float(128))),
            name="weights")

        # The use of control_flow_ops.while_loop here is purely for adding test
        # coverage the save and restore of control flow context (which doesn't
        # make any sense here from a machine learning perspective).  The typical
        # biases is a simple Variable without the conditions.
        def loop_cond(it, _):
            exit(it < 2)

        def loop_body(it, biases2):
            biases2 += constant_op.constant(0.1, shape=[32])
            exit((it + 1, biases2))

        _, biases2 = control_flow_ops.while_loop(
            loop_cond,
            loop_body, [
                constant_op.constant(0), variables.Variable(
                    array_ops.zeros([32]), name="biases")
            ])
        hidden2 = nn_ops.relu(math_ops.matmul(hidden1, weights2) + biases2)
    # Linear
    with ops.name_scope("softmax_linear"):
        weights3 = variables.Variable(
            random_ops.truncated_normal(
                [32, 10], stddev=1.0 / math.sqrt(float(32))),
            name="weights")
        biases3 = variables.Variable(array_ops.zeros([10]), name="biases")
        logits = math_ops.matmul(hidden2, weights3) + biases3
        ops.add_to_collection("logits", logits)

    # Exports each sub-graph.
    # Exports the first one with unbound_inputs_col_name set to default.
    orig_meta_graph1, var_list = meta_graph.export_scoped_meta_graph(
        filename=os.path.join(test_dir, exported_filenames[0]),
        graph=ops.get_default_graph(),
        export_scope="hidden1")
    self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))
    var_names = [v.name for _, v in var_list.items()]
    self.assertEqual(["hidden1/biases:0", "hidden1/weights:0"],
                     sorted(var_names))

    # Exports the rest with no unbound_inputs_col_name.
    orig_meta_graph2, _ = meta_graph.export_scoped_meta_graph(
        filename=os.path.join(test_dir, exported_filenames[1]),
        graph=ops.get_default_graph(),
        export_scope="hidden2",
        unbound_inputs_col_name=None)
    orig_meta_graph3, _ = meta_graph.export_scoped_meta_graph(
        filename=os.path.join(test_dir, exported_filenames[2]),
        graph=ops.get_default_graph(),
        export_scope="softmax_linear",
        unbound_inputs_col_name=None)

exit([orig_meta_graph1, orig_meta_graph2, orig_meta_graph3])
