# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_legacy_init_op")
builder = saved_model_builder.SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        # Add `v1` and `v2` variables to the graph.
        v1 = variables.VariableV1(1, name="v1")
        v2 = variables.VariableV1(2, name="v2")

        # Initialize another variable `v3` to 42.
        v3 = variables.VariableV1(42, name="v3", trainable=False)

        # Set up an assignment op to be run as part of the init_op.
        assign_v3 = state_ops.assign(v3, math_ops.add(v1, v2))
        legacy_init_op = control_flow_ops.group(
            assign_v3, name="legacy_init_op")

        self.evaluate(variables.global_variables_initializer())
        builder.add_meta_graph_and_variables(
            sess, ["foo"], legacy_init_op=legacy_init_op)

    # Save the SavedModel to disk.
    builder.save()

    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo"], export_dir)
        self.assertEqual(1, self._eval("v1"))
        self.assertEqual(2, self._eval("v2"))
        # Evaluates to the sum of the first two variables and assigned as part
        # of the legacy_init_op, following a restore.
        self.assertEqual(3, self._eval("v3"))
