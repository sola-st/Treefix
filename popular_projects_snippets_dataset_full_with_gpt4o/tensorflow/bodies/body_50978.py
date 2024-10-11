# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_collections")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Graph with a single variable added to a collection. SavedModel invoked
    # to:
    # - add with weights.
    with self.session(graph=ops.Graph()) as sess:
        v = variables.VariableV1(42, name="v")
        ops.add_to_collection("foo_vars", v)
        self.evaluate(variables.global_variables_initializer())
        self.assertEqual(42, self.evaluate(v))
        builder.add_meta_graph_and_variables(sess, ["foo"])

    # Graph with the same single variable added to a different collection.
    # SavedModel invoked to:
    # - simply add the model (weights are not updated).
    with self.session(graph=ops.Graph()) as sess:
        v = variables.VariableV1(43, name="v")
        ops.add_to_collection("bar_vars", v)
        self.evaluate(variables.global_variables_initializer())
        self.assertEqual(43, self.evaluate(v))
        builder.add_meta_graph(["bar"])

    # Save the SavedModel to disk.
    builder.save()

    # Restore the graph with tag "foo", whose variables were saved. The
    # collection 'foo_vars' should contain a single element. The collection
    # 'bar_vars' should not be found.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo"], export_dir)
        collection_foo_vars = ops.get_collection("foo_vars")
        self.assertEqual(len(collection_foo_vars), 1)
        self.assertEqual(42, self._eval(collection_foo_vars[0]))

        self.assertEqual(len(ops.get_collection("bar_vars")), 0)

    # Restore the graph with tag "bar", whose variables were not saved. The
    # collection-def exported as part of the meta graph def is updated to
    # reflect the new collection. The value of the variable in the
    # collection-def corresponds to the saved value (from the previous graph
    # with tag "foo").
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["bar"], export_dir)
        collection_bar_vars = ops.get_collection("bar_vars")
        self.assertEqual(len(collection_bar_vars), 1)
        self.assertEqual(42, self._eval(collection_bar_vars[0]))

        self.assertEqual(len(ops.get_collection("foo_vars")), 0)
