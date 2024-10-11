# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_graph_has_variables")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Graph with no variables.
    with self.session(graph=ops.Graph()) as sess:
        constant_5_name = constant_op.constant(5.0).name
        builder.add_meta_graph_and_variables(sess, ["foo"])

    # Second graph with no variables
    with self.session(graph=ops.Graph()) as sess:
        constant_6_name = constant_op.constant(6.0).name
        builder.add_meta_graph(["bar"])

    # Save the SavedModel to disk.
    builder.save()

    # Restore the graph with tag "foo".
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo"], export_dir)
        # Read the constant a from the graph.
        a = ops.get_default_graph().get_tensor_by_name(constant_5_name)
        b = constant_op.constant(6.0)
        c = a * b
        self.assertEqual(30.0, self.evaluate(c))

    # Restore the graph with tag "bar".
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["bar"], export_dir)
        # Read the constant a from the graph.
        a = ops.get_default_graph().get_tensor_by_name(constant_6_name)
        b = constant_op.constant(5.0)
        c = a * b
        self.assertEqual(30.0, self.evaluate(c))
