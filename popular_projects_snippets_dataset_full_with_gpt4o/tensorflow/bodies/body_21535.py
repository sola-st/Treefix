# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("good_collection")
filename = os.path.join(test_dir, "metafile")
with self.cached_session():
    # Creates a graph.
    v0 = variables.VariableV1(1.0, name="v0")
    control_flow_ops.cond(
        math_ops.less(v0, 10), lambda: math_ops.add(v0, 1),
        lambda: math_ops.subtract(v0, 1))
    control_flow_ops.while_loop(lambda i: math_ops.less(i, 10),
                                lambda i: math_ops.add(i, 1), [v0])
    var = variables.VariableV1(constant_op.constant(0, dtype=dtypes.int64))
    count_up_to = var.count_up_to(3)
    input_queue = data_flow_ops.FIFOQueue(
        30, dtypes.float32, shared_name="collection_queue")
    qr = queue_runner_impl.QueueRunner(input_queue, [count_up_to])
    variables.global_variables_initializer()
    # Creates a saver.
    save = saver_module.Saver({"v0": v0})
    # Adds a set of collections.
    ops_lib.add_to_collection("int_collection", 3)
    ops_lib.add_to_collection("float_collection", 3.5)
    ops_lib.add_to_collection("string_collection", "hello")
    ops_lib.add_to_collection("variable_collection", v0)
    # Add QueueRunners.
    queue_runner_impl.add_queue_runner(qr)
    # Adds user_defined proto in three formats: string, bytes and Any.
    queue_runner = queue_runner_pb2.QueueRunnerDef(queue_name="test_queue")
    ops_lib.add_to_collection("user_defined_string_collection",
                              str(queue_runner))
    ops_lib.add_to_collection("user_defined_bytes_collection",
                              queue_runner.SerializeToString())
    any_buf = Any()
    any_buf.Pack(queue_runner)
    ops_lib.add_to_collection("user_defined_any_collection", any_buf)

    # Generates MetaGraphDef.
    meta_graph_def = save.export_meta_graph(filename)
    self.assertTrue(meta_graph_def.HasField("saver_def"))
    self.assertTrue(meta_graph_def.HasField("graph_def"))
    self.assertTrue(meta_graph_def.HasField("meta_info_def"))
    self.assertNotEqual(meta_graph_def.meta_info_def.tensorflow_version, "")
    self.assertNotEqual(meta_graph_def.meta_info_def.tensorflow_git_version,
                        "")
    collection_def = meta_graph_def.collection_def
    self.assertEqual(len(collection_def), 12)

with ops_lib.Graph().as_default():
    # Restores from MetaGraphDef.
    new_saver = saver_module.import_meta_graph(filename)
    # Generates a new MetaGraphDef.
    new_meta_graph_def = new_saver.export_meta_graph()
    # It should be the same as the original.

test_util.assert_meta_graph_protos_equal(
    self, meta_graph_def, new_meta_graph_def)
