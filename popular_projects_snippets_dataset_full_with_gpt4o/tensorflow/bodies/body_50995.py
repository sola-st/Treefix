# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_op")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with session.Session(
        graph=ops.Graph(),
        config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
        with sess.graph.device("/cpu:0"):
            v1 = variables.VariableV1(1, name="v1")
        with sess.graph.device("/cpu:1"):
            v2 = variables.VariableV1(2, name="v2")

        # v3 is an unsaved variable derived from v1 and v2.  It is used to
        # exercise the ability to run an init op when restoring a graph.
        v3 = variables.VariableV1(1, name="v3", trainable=False, collections=[])
        assign_v3 = state_ops.assign(v3, math_ops.add(v1, v2))
        control_flow_ops.group(assign_v3, name="init_op")

        self.evaluate(variables.global_variables_initializer())
        self.assertEqual(1, self._eval("v1"))
        self.assertEqual(2, self._eval("v2"))

        builder.add_meta_graph_and_variables(sess, ["foo"])

    # Save the SavedModel to disk.
    builder.save()

    with session.Session(
        graph=ops.Graph(),
        config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
        loader.load(sess, ["foo"], export_dir)

        # Validate variables, run the init op and verify result.
        self.assertEqual(1, self._eval("v1"))
        self.assertEqual(2, self._eval("v2"))
        sess.run("init_op")
        self.assertEqual(3, self._eval("v3"))
