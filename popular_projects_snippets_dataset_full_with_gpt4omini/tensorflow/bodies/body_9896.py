# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_utils_test.py
saved_model_dir = os.path.join(test.get_temp_dir(), "test_tags")
builder = saved_model_builder.SavedModelBuilder(saved_model_dir)
# Force test to run in graph mode since SavedModelBuilder.save requires a
# session to work.
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

    # Graph that updates the single variable. SavedModel is invoked:
    # - to add the model (weights are not updated).
    # - multiple predefined tags.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 44)
        builder.add_meta_graph([tag_constants.SERVING, tag_constants.GPU])

    # Graph that updates the single variable. SavedModel is invoked:
    # - to add the model (weights are not updated).
    # - multiple predefined tags for serving on TPU.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 44)
        builder.add_meta_graph([tag_constants.SERVING, tag_constants.TPU])

    # Graph that updates the single variable. SavedModel is invoked:
    # - to add the model (weights are not updated).
    # - multiple custom tags.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 45)
        builder.add_meta_graph(["foo", "bar"])

    # Save the SavedModel to disk.
    builder.save()

actual_tags = saved_model_utils.get_saved_model_tag_sets(saved_model_dir)
expected_tags = [["train"], ["serve"], ["serve", "gpu"], ["serve", "tpu"],
                 ["foo", "bar"]]
self.assertEqual(expected_tags, actual_tags)
