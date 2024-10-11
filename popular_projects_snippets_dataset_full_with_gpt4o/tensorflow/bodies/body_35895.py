# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
save_prefix = os.path.join(self.get_temp_dir(), "ckpt")
save_graph = ops.Graph()
with save_graph.as_default(), self.session(
    graph=save_graph) as session:
    partitioner = partitioned_variables.fixed_size_partitioner(5, axis=0)
    with variable_scope.variable_scope("root", partitioner=partitioner):
        v0 = variable_scope.get_variable(
            "v0", dtype=dtypes.float32, shape=(10, 10))
        v0_list = v0._get_variable_list()
        v0_part = v0._get_partitions()
        self.assertEqual(len(v0_list), 5)
        self.assertAllEqual(v0_part, (5, 1))
        self.evaluate(variables.global_variables_initializer())

        save_graph.get_collection_ref("partvar").append(v0)
        saver = saver_lib.Saver()
        save_graph.finalize()
        save_path = saver.save(sess=session, save_path=save_prefix)
        previous_value = session.run(
            save_graph.get_tensor_by_name(v0.name + ":0"))

restore_graph = ops.Graph()
with restore_graph.as_default(), self.session(
    graph=restore_graph) as session:
    saver = saver_lib.import_meta_graph(save_path + ".meta")
    saver.restore(sess=session, save_path=save_path)
    v0, = save_graph.get_collection_ref("partvar")
    self.assertIsInstance(v0, variables.PartitionedVariable)
    self.assertAllEqual(
        previous_value,
        session.run(restore_graph.get_tensor_by_name(v0.name + ":0")))
