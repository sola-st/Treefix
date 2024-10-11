# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_train_op")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        # Add `v1` and `v2` variables to the graph.
        v1 = variables.VariableV1(1, name="v1")
        v2 = variables.VariableV1(2, name="v2")

        self.evaluate(variables.global_variables_initializer())
        train_op = state_ops.assign_add(v1, v2)

        self.evaluate(train_op)
        builder.add_meta_graph_and_variables(sess, ["foo"], train_op=train_op)

    # Save the SavedModel to disk.
    builder.save()

    with self.session(graph=ops.Graph()) as sess:
        meta_graph_def = loader.load(sess, ["foo"], export_dir)
        self.assertEqual(3, self._eval("v1"))
        self.assertEqual(2, self._eval("v2"))
        if variable_scope.resource_variables_enabled():
            self.assertEqual(
                loader_impl.get_train_op(meta_graph_def).type,
                "AssignAddVariableOp")
        else:
            self.assertIsInstance(
                loader_impl.get_train_op(meta_graph_def), ops.Tensor)
