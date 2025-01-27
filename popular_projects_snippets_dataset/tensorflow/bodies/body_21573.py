# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
graph = ops_lib.Graph()
with graph.as_default():
    # Creates an inference graph.
    # Hidden 1
    images = constant_op.constant(
        1.2, dtypes.float32, shape=[100, 28], name="images")
    with ops_lib.name_scope("hidden1"):
        weights1 = variables.VariableV1(
            random_ops.truncated_normal(
                [28, 128], stddev=1.0 / math.sqrt(float(28))),
            name="weights")
        # The use of control_flow_ops.cond here is purely for adding test
        # coverage the save and restore of control flow context (which doesn't
        # make any sense here from a machine learning perspective).  The typical
        # biases is a simple Variable without the conditions.
        biases1 = variables.VariableV1(
            control_flow_ops.cond(
                math_ops.less(random.random(), 0.5),
                lambda: array_ops.ones([128]), lambda: array_ops.zeros([128])),
            name="biases")
        hidden1 = nn_ops.relu(math_ops.matmul(images, weights1) + biases1)

    # Hidden 2
    with ops_lib.name_scope("hidden2"):
        weights2 = variables.VariableV1(
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

        _, biases2 = control_flow_ops.while_loop(loop_cond, loop_body, [
            constant_op.constant(0), variables.VariableV1(array_ops.zeros([32]))
        ])
        hidden2 = nn_ops.relu(math_ops.matmul(hidden1, weights2) + biases2)
    # Linear
    with ops_lib.name_scope("softmax_linear"):
        weights3 = variables.VariableV1(
            random_ops.truncated_normal(
                [32, 10], stddev=1.0 / math.sqrt(float(32))),
            name="weights")
        biases3 = variables.VariableV1(array_ops.zeros([10]), name="biases")
        logits = math_ops.matmul(hidden2, weights3) + biases3
        ops_lib.add_to_collection("logits", logits)

        # Adds user_defined proto in three formats: string, bytes and Any.
        # Any proto should just pass through.
        queue_runner = queue_runner_pb2.QueueRunnerDef(queue_name="test_queue")
        ops_lib.add_to_collection("user_defined_string_collection",
                                  str(queue_runner))
        ops_lib.add_to_collection("user_defined_bytes_collection",
                                  queue_runner.SerializeToString())
        any_buf = Any()
        any_buf.Pack(queue_runner)
        ops_lib.add_to_collection("user_defined_any_collection", any_buf)

    _, var_list = meta_graph.export_scoped_meta_graph(
        filename=os.path.join(test_dir, exported_filename),
        graph=ops_lib.get_default_graph(),
        export_scope="hidden1")
    self.assertEqual(["biases:0", "weights:0"], sorted(var_list.keys()))

with graph.as_default(), self.session() as sess:
    self.evaluate(variables.global_variables_initializer())
    saver = saver_module.Saver(var_list=var_list, max_to_keep=1)
    saver.save(sess, os.path.join(test_dir, ckpt_filename), write_state=False)
