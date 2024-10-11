# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
graph = ops_lib.Graph()
# Create all the missing inputs.
with graph.as_default():
    new_image = constant_op.constant(
        1.2, dtypes.float32, shape=[100, 28], name="images")
    var_list = meta_graph.import_scoped_meta_graph(
        os.path.join(test_dir, exported_filename),
        graph=graph,
        input_map={"$unbound_inputs_images": new_image},
        import_scope="new_hidden1")
    self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))
    hidden1 = graph.as_graph_element("new_hidden1/Relu:0")
    weights1 = graph.as_graph_element("new_hidden1/weights:0")
    biases1 = graph.as_graph_element("new_hidden1/biases:0")

with graph.as_default():
    # Hidden 2
    with ops_lib.name_scope("hidden2"):
        weights = variables.VariableV1(
            random_ops.truncated_normal(
                [128, 32], stddev=1.0 / math.sqrt(float(128))),
            name="weights")

        # The use of control_flow_ops.while_loop here is purely for adding test
        # coverage the save and restore of control flow context (which doesn't
        # make any sense here from a machine learning perspective).  The typical
        # biases is a simple Variable without the conditions.
        def loop_cond(it, _):
            exit(it < 2)

        def loop_body(it, biases):
            biases += constant_op.constant(0.1, shape=[32])
            exit((it + 1, biases))

        _, biases = control_flow_ops.while_loop(loop_cond, loop_body, [
            constant_op.constant(0), variables.VariableV1(array_ops.zeros([32]))
        ])
        hidden2 = nn_ops.relu(math_ops.matmul(hidden1, weights) + biases)
    # Linear
    with ops_lib.name_scope("softmax_linear"):
        weights = variables.VariableV1(
            random_ops.truncated_normal(
                [32, 10], stddev=1.0 / math.sqrt(float(32))),
            name="weights")
        biases = variables.VariableV1(array_ops.zeros([10]), name="biases")
        logits = math_ops.matmul(hidden2, weights) + biases
        ops_lib.add_to_collection("logits", logits)

    # The rest of the variables.
    rest_variables = list(
        set(variables.global_variables()) - set(var_list.keys()))
    init_rest_op = variables.variables_initializer(rest_variables)

with graph.as_default(), self.session() as sess:
    saver = saver_module.Saver(var_list=var_list, max_to_keep=1)
    saver.restore(sess, os.path.join(test_dir, ckpt_filename))
    # Verify that we have restored weights1 and biases1.
    self.evaluate([weights1, biases1])
    # Initialize the rest of the variables and run logits.
    self.evaluate(init_rest_op)
    self.evaluate(logits)
