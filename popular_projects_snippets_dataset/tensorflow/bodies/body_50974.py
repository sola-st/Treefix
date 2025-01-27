# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_variables")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Graph with two variables. SavedModel invoked to:
    # - add with weights.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v1", 1)
        self._init_and_validate_variable(sess, "v2", 2)
        builder.add_meta_graph_and_variables(sess, ["foo"])

    # Graph with a single variable (subset of the variables from the previous
    # graph whose weights were saved). SavedModel invoked to:
    # - simply add the model (weights are not updated).
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v2", 3)
        builder.add_meta_graph(["bar"])

    # Graph with a single variable (disjoint set of variables from the
    # previous graph whose weights were saved). SavedModel invoked to:
    # - simply add the model (weights are not updated).
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v3", 4)
        builder.add_meta_graph(["baz"])

    # Save the SavedModel to disk.
    builder.save()

    # Restore the graph with tag "foo", whose variables were saved.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo"], export_dir)
        collection_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
        self.assertEqual(len(collection_vars), 2)
        self.assertEqual(1, self._eval(collection_vars[0]))
        self.assertEqual(2, self._eval(collection_vars[1]))

    # Restore the graph with tag "bar", whose variables were not saved. Only
    # the subset of the variables added to the graph will be restored with the
    # checkpointed value.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["bar"], export_dir)
        collection_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
        self.assertEqual(len(collection_vars), 1)
        self.assertEqual(2, self._eval(collection_vars[0]))

    # Try restoring the graph with tag "baz", whose variables were not saved.
    # Since this graph has a disjoint set of variables from the set that was
    # saved, this should raise an error.
    with self.session(graph=ops.Graph()) as sess:
        self.assertRaises(errors.NotFoundError, loader.load, sess, ["baz"],
                          export_dir)
