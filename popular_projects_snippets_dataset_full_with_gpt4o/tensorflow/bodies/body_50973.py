# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_tags")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Graph with a single variable. SavedModel invoked to:
    # - add with weights.
    # - a single tag (from predefined constants).
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)
        builder.add_meta_graph_and_variables(sess, [tag_constants.TRAINING])

    # Graph that updates the single variable. SavedModel invoked to:
    # - simply add the model (weights are not updated).
    # - a single tag (from predefined constants).
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 43)
        builder.add_meta_graph([tag_constants.SERVING])

    # Graph that updates the single variable. SavedModel invoked to:
    # - simply add the model (weights are not updated).
    # - multiple tags (from predefined constants).
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 45)
        builder.add_meta_graph([tag_constants.SERVING, tag_constants.GPU])

    # Graph that updates the single variable. SavedModel invoked to:
    # - simply add the model (weights are not updated).
    # - multiple tags (from predefined constants for serving on TPU).
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 45)
        builder.add_meta_graph([tag_constants.SERVING, tag_constants.TPU])

    # Graph that updates the single variable. SavedModel is invoked:
    # - to add the model (weights are not updated).
    # - multiple custom tags.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 44)
        builder.add_meta_graph(["foo", "bar"])

    # Save the SavedModel to disk.
    builder.save()

    # Restore the graph with a single predefined tag whose variables were
    # saved.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, [tag_constants.TRAINING], export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))

    # Restore the graph with a single predefined tag whose variables were not
    # saved.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, [tag_constants.SERVING], export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))

    # Restore the graph with multiple predefined tags whose variables were not
    # saved.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, [tag_constants.SERVING, tag_constants.GPU],
                    export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))

    # Restore the graph with multiple predefined tags (for serving on TPU)
    # whose variables were not saved.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, [tag_constants.SERVING, tag_constants.TPU],
                    export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))

    # Restore the graph with multiple tags. Provide duplicate tags to test set
    # semantics.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, ["foo", "bar", "foo"], export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))

    # Try restoring a graph with a non-existent tag. This should yield a
    # runtime error.
    with self.session(graph=ops.Graph()) as sess:
        self.assertRaises(RuntimeError, loader.load, sess, ["INVALID"],
                          export_dir)

    # Try restoring a graph where a subset of the tags match. Since tag
    # matching for meta graph defs follows "all" semantics, this should yield
    # a runtime error.
    with self.session(graph=ops.Graph()) as sess:
        self.assertRaises(RuntimeError, loader.load, sess, ["foo", "baz"],
                          export_dir)
