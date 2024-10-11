# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
with export_graph.as_default():
    partitioned_var = variable_scope.get_variable(
        "a", shape=[6], initializer=init_ops.constant_initializer(13),
        partitioner=partitioned_variables.fixed_size_partitioner(2),
        use_resource=True)
    x = array_ops.placeholder(shape=[], dtype=dtypes.float32)
    y = x * partitioned_var
    with session_lib.Session() as session:
        session.run(variables.global_variables_initializer())
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(session, path,
                                inputs={"x": x}, outputs={"y": y})

        # Create a name-based checkpoint with different values.
        session.run(partitioned_var.assign([[5, 4, 3], [2, 1, 0]]))
        ckpt_path = os.path.join(self.get_temp_dir(), "restore_ckpt")
        saver.Saver().save(session, ckpt_path)

imported = load.load(path)
self.assertAllClose(self.evaluate(imported.variables),
                    [[13, 13, 13], [13, 13, 13]])

self.evaluate(imported.restore(ckpt_path))
self.assertAllClose(self.evaluate(imported.variables),
                    [[5, 4, 3], [2, 1, 0]])
self.assertAllClose(
    self.evaluate(
        imported.signatures["serving_default"](constant_op.constant(2.))),
    {"y": [10, 8, 6, 4, 2, 0]})
