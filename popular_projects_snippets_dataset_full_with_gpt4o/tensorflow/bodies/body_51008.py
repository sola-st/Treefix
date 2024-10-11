# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
builder = saved_model_builder.SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session() as sess:
        # Initialize variable `v1` to 1.
        v1 = variables.VariableV1(1, name="v1")
        ops.add_to_collection("v", v1)

        # Initialize another variable `v2` to 42.
        v2 = variables.VariableV1(
            42, name="v2", trainable=False, collections=[])
        ops.add_to_collection("v", v2)

        # Set up an assignment op to be run as part of the init op.
        assign_v2 = state_ops.assign(v2, v1)
        init_op = control_flow_ops.group(assign_v2, name="init_op")

        self.evaluate(variables.global_variables_initializer())

        ops.add_to_collection(key, control_flow_ops.no_op())
        # ValueError should be raised since the LEGACY_INIT_OP_KEY collection
        # is not empty and we don't support multiple init ops.
        with self.assertRaisesRegex(ValueError, "Graph already contains"):
            builder.add_meta_graph_and_variables(
                sess, ["foo"], legacy_init_op=init_op)
        # We shouldn't be able to add as MAIN_OP, either.
        with self.assertRaisesRegex(ValueError, "Graph already contains"):
            builder.add_meta_graph_and_variables(sess, ["foo"], main_op=init_op)
